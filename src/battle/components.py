import random
import re
import sys
from typing import Callable, Dict, Optional, Union

import streamlit as st
from autogen import GroupChat, GroupChatManager, Agent, ConversableAgent


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

    def _get_text_color(self, bg_color):
        """Calculate the luminance of the background color and return a suitable text color."""
        r, g, b = int(bg_color[1:3], 16), int(bg_color[3:5], 16), int(bg_color[5:7], 16)
        luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
        return 'white' if luminance < 0.5 else 'black'

    def _sanitize_message(self, message: str, agent_name: str) -> str:
        print('\n\nmessage: ', message)
        print('\n\nagent_name: ', agent_name)

        pattern = re.compile(rf"^{re.escape(agent_name)}:?\s*", re.IGNORECASE)
        sanitized_message = re.sub(pattern, '', message)
        
        return sanitized_message

    def _process_received_message(self, message, sender, silent):
        agent_alignment = {"Right": "agent-right", "Left": "agent-left"}
        if isinstance(message, str):
            message = self._sanitize_message(message, sender.name)
            if sender.name != "chat_manager":
                agent_role = next((role for name, _, _, _, role in st.session_state.agents if name == sender.name), "")
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
                    random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
                    text_color = self._get_text_color(random_color)

                    with st.chat_message(sender.name):
                        st.markdown(
                            f"<div class='message-row {agent_alignment.get(agent_role, '')}'>"
                            f"<span class='agent-name'>{sender.name}</span>"
                            f"<div class='chat-bubble' style='background-color: {random_color}; color: {text_color};'>{message}</div>"
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
