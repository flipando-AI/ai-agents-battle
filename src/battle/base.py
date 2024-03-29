import os
from typing import List

import streamlit as st
from autogen import AssistantAgent, ConversableAgent, GroupChat, UserProxyAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import \
    RetrieveUserProxyAgent
from chromadb.utils import embedding_functions

from src.battle.components import (AgentPlus, GroupChatManagerPlus,
                                   UserProxyAgentPlus)
from src.battle.prompts import (chat_manager_prompt_whi,
                                chat_manager_prompt_wohi)


class GroupDiscussion:
    def __init__(
        self, 
        agents: List[AgentPlus], 
        extra_knowledge: List[str], 
        human_feedback: bool, 
        model_name: str, 
        seed: int
    ):
        self.agents = agents
        self.seed = seed
        self.extra_knowledge = extra_knowledge
        self.human_feedback = human_feedback
        self.termination_msg = lambda x: isinstance(x, dict) and "TERMINATE" == str(x.get("content", ""))[-9:].upper()
        self.embedding_function = embedding_functions.OpenAIEmbeddingFunction(
            api_key=st.session_state.api_key,
            model_name="text-embedding-ada-002"
        )
        self.retriever_assistant = self._create_retriever_assistant()
        self.llm_config = self._fetch_model_config(model_name)

    def _fetch_model_config(self, model_name: str):
        with_retriever = True if self.retriever_assistant else False
        if model_name == "gpt-35-turbo-16k":
            config_list = [
                {
                    "model": model_name, 
                    "api_type": "azure", 
                    "api_key": os.getenv("AZURE_API_KEY"),
                    "api_base": os.getenv("AZURE_API_BASE"),
                    "api_version": os.getenv("AZURE_API_VERSION"),
                }
            ]
        else:
            config_list = [{"model": model_name, "api_key": st.session_state.api_key}]

        llm_config = {
            "request_timeout": 600,
            "config_list": config_list,
            "seed": self.seed,
        }

        if with_retriever:
            llm_config["functions"] = [
                {
                    "name": "retrieve_content",
                    "description": "retrieve content for code generation and question answering.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "message": {
                                "type": "string",
                                "description": "Refined message which keeps the original meaning and can be used to retrieve content for code generation and question answering.",
                            }
                        },
                        "required": ["message"],
                    },
                }
            ]

        return llm_config

    def _retrieve_content(self, message, n_results=3):
            self.retriever_assistant.n_results = n_results
            update_context_case1, update_context_case2 = self.retriever_assistant._check_update_context(message)
            if (update_context_case1 or update_context_case2) and self.retriever_assistant.update_context:
                self.retriever_assistant.problem = message if not hasattr(self.retriever_assistant, "problem") else self.retriever_assistant.problem
                _, ret_msg = self.retriever_assistant._generate_retrieve_user_reply(message)
            else:
                ret_msg = self.retriever_assistant.generate_init_message(message, n_results=n_results)
            return ret_msg if ret_msg else message

    def _create_retriever_assistant(self):
        if self.extra_knowledge:
            return RetrieveUserProxyAgent(
                name="Retrieval_Assistant",
                is_termination_msg=self.termination_msg,
                system_message="Assistant who has extra content retrieval power for solving difficult problems.",
                human_input_mode="NEVER",
                max_consecutive_auto_reply=3,
                retrieve_config={
                    "task": "qa",
                    "docs_path": self.extra_knowledge,
                    "embedding_function": self.embedding_function,
                    "chunk_token_size": 256,
                    "get_or_create": True
                },
                code_execution_config=False,
            )
        else:
            return None

    def _init_agent(self, agent: AgentPlus) -> AssistantAgent:
        prompt = f"{agent.prompt}\n\n\nNote: Do not start your messages stating your name, the agents already know who you are. Its crucial that you respond your plain message alone"
        if agent.code_execution:
            return UserProxyAgent(
                name=agent.name,
                system_message=prompt,
                code_execution_config={"last_n_messages": 2, "work_dir": "groupchat"},
                human_input_mode="NEVER",
                is_termination_msg=self.termination_msg,
                llm_config=self._fetch_model_config(agent.model),
            )

        else:
            return AssistantAgent(
                name=agent.name,
                system_message=prompt,
                llm_config=self._fetch_model_config(agent.model),
                is_termination_msg=self.termination_msg
            )

    def _assemble_agents(self) -> List[AssistantAgent]:
        agents = [self._init_agent(agent) for agent in self.agents]
        if self.retriever_assistant:
            for agent in agents:
                agent.register_function(
                    function_map={
                        "retrieve_content": self._retrieve_content,
                    }
                )

        agents = agents + [self.retriever_assistant] if self.retriever_assistant else agents
        agent_names = ", ".join([agent.name for agent in agents])

        return agents, agent_names
    
    def _create_user_proxy(self) -> UserProxyAgentPlus:
        if self.human_feedback:
            input_mode = "ALWAYS"
            message = "You ask questions and/or give tasks to the agents. You are the conversation initiator and you may intervene at any time to steer the conversation in the right direction."
        else:
            input_mode = "NEVER"
            message = "You ask questions and/or give tasks to the agents. You are the conversation initiator. You should NEVER intervene during the conversation. Your only role is to start the conversation and let the agents do the rest."

        user_proxy = UserProxyAgentPlus(
            name="USER",
            system_message=message,
            human_input_mode=input_mode,
            is_termination_msg=self.termination_msg,
            llm_config=self.llm_config,
        )
        if self.retriever_assistant:
            user_proxy.register_function(
                function_map={
                    "retrieve_content": self._retrieve_content,
                }
            )

        return user_proxy

    def assemble_groupchat(self, num_rounds: int) -> ConversableAgent:
        agents, agent_names = self._assemble_agents()
        user_proxy = self._create_user_proxy()

        groupchat = GroupChat(
            agents=[user_proxy] + agents, 
            messages=[], 
            max_round=num_rounds
        )
        manager_prompt = chat_manager_prompt_whi if self.human_feedback else chat_manager_prompt_wohi
        manager = GroupChatManagerPlus(
            name="chat_manager",
            groupchat=groupchat, 
            system_message=manager_prompt.format(agents=agent_names),
            llm_config=self.llm_config,
            is_termination_msg=self.termination_msg
        )

        return user_proxy, manager
