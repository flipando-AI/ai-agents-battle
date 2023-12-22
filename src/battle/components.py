import re
import sys
from typing import Callable, Dict, Optional, Union

import streamlit as st
from autogen import Agent, ConversableAgent, GroupChat, GroupChatManager
from pydantic import BaseModel


class AgentPlus(BaseModel):
    name: str
    prompt: str
    model: str
    code_execution: bool
    chat_side: str


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

    def _fetch_agent_color(self, agent_name: str) -> str:
        chat_side = ""
        bkg_color = ""
        txt_color = ""
        for tup in st.session_state.agents:
            if tup[0] == agent_name:
                chat_side, bkg_color, txt_color =  tup[4], tup[5], tup[6]

        return chat_side, bkg_color, txt_color

    def _sanitize_message(self, message: str, agent_name: str) -> str:
        pattern = re.compile(rf"^{re.escape(agent_name)}:?\s*", re.IGNORECASE)
        sanitized_message = re.sub(pattern, '', message)
        
        return sanitized_message

    def _process_received_message(self, message, sender, silent):
        agent_alignment = {"Right": "agent-right", "Left": "agent-left"}
        if isinstance(message, str):
            message = self._sanitize_message(message, sender.name)
            if sender.name != "chat_manager":
                agent_side, bkg_color, txt_color = self._fetch_agent_color(sender.name)
                if sender.name == "USER":
                    if message:
                        with st.chat_message(sender.name):
                            st.markdown(
                                f"<div class='user-message'>"
                                f"<div class='chat-bubble user-bubble'>{message}</div>"
                                f"</div>",
                                unsafe_allow_html=True
                            )

                else:
                    with st.chat_message(sender.name):
                        st.markdown(
                            f"<div class='message-row {agent_alignment.get(agent_side, '')}'>"
                            f"<span class='agent-name'>{sender.name}</span>"
                            f"<div class='chat-bubble' style='background-color: {bkg_color}; color: {txt_color};'>{message}</div>"
                            f"</div>",
                            unsafe_allow_html=True
                        )

        return super()._process_received_message(message, sender, silent)


class UserProxyAgentPlus(ConversableAgent):
    def __init__(
        self,
        name: str,
        is_termination_msg: Optional[Callable[[Dict], bool]] = None,
        max_consecutive_auto_reply: Optional[int] = None,
        human_input_mode: Optional[str] = "ALWAYS",
        function_map: Optional[Dict[str, Callable]] = None,
        code_execution_config: Optional[Union[Dict, bool]] = None,
        default_auto_reply: Optional[Union[str, Dict, None]] = "",
        llm_config: Optional[Union[Dict, bool]] = False,
        system_message: Optional[str] = "",
        group_chat: Optional[bool] = False,
    ):    
        super().__init__(
            name,
            system_message,
            is_termination_msg,
            max_consecutive_auto_reply,
            human_input_mode,
            function_map,
            code_execution_config,
            llm_config,
            default_auto_reply,
        )
        self.group_chat = group_chat

    def get_human_input(self, prompt: str) -> str:
        """Get human input.

        Override this method to customize the way to get human input.

        Args:
            prompt (str): prompt for the human input.

        Returns:
            str: human input.
        """
        st.markdown("<div class='waiting-input'> Awaiting human input (in console)</div>", unsafe_allow_html=True)
        reply = input(prompt)
        return reply
