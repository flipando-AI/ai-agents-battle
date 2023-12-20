import sys
from typing import Dict, List, Optional, Union, Tuple

import streamlit as st
from autogen import (Agent, AssistantAgent, GroupChat, GroupChatManager,
                     config_list_from_json)

from src.prompts import system_message_chat_manager


class GroupChatManagerPlus(GroupChatManager):
    def __init__(
        self,
        groupchat: GroupChat,
        name: Optional[str] = "chat_manager",
        max_consecutive_auto_reply: Optional[int] = sys.maxsize,
        human_input_mode: Optional[str] = "NEVER",
        system_message: Optional[str] = "Enhanced group chat manager.",
        llm_config: Optional[Union[Dict, bool]] = None,
        **kwargs,
    ):
        super().__init__(
            groupchat=groupchat,
            name=name,
            max_consecutive_auto_reply=max_consecutive_auto_reply,
            human_input_mode=human_input_mode,
            system_message=system_message,
            llm_config=llm_config,
            **kwargs,
        )
        self.register_reply(Agent, GroupChatManager.run_chat, config=groupchat, reset_config=GroupChat.reset)

    def _process_received_message(self, message, sender, silent):
        agent_alignment = {"Right": "agent-right", "Left": "agent-left"}

        if sender.name != "chat_manager":
            agent_role = next((role for name, prompt, role in st.session_state.agents if name == sender.name), "")

            with st.chat_message(sender.name):
                st.markdown(
                    f"<div class='message-row {agent_alignment.get(agent_role, '')}'>"
                    f"<span class='agent-name'>{sender.name}</span>"
                    f"<div class='chat-bubble'>{message}</div>"
                    f"</div>",
                    unsafe_allow_html=True
                )

        return super()._process_received_message(message, sender, silent)


def fetch_model_config(model_name: str):
    config_list = config_list_from_json(
        env_or_file="OAI_CONFIG_LIST", 
        filter_dict={
            "model": [
                model_name,
            ]
        }
    )

    return {
        "request_timeout": 600,
        "config_list": config_list,
        "seed": 42,
    }


class GroupDiscussion:
    def __init__(self, agents: List[Tuple[str, str]], llm_config: Dict):
        self.agents = agents
        self.llm_config = llm_config

    def _init_agent(self, name: str, prompt: str) -> AssistantAgent:
        return AssistantAgent(
            name=name,
            system_message=prompt,
            llm_config=self.llm_config,
            is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),
        )

    def _assemble_agents(self) -> List[AssistantAgent]:
        return [self._init_agent(name, prompt) for name, prompt in self.agents]
    
    def assemble_groupchat(self, num_rounds: int) -> GroupChatManagerPlus:
        agents = self._assemble_agents()
        groupchat = GroupChat(
            agents=agents, 
            messages=[], 
            max_round=num_rounds
        )

        manager = GroupChatManagerPlus(
            name="chat_manager",
            groupchat=groupchat, 
            llm_config=self.llm_config,
            is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),
            system_message=system_message_chat_manager
        )

        return manager
