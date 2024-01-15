import random
from typing import List, Tuple

import streamlit as st

from src.battle.base import GroupDiscussion
from src.battle.components import AgentPlus
from src.utils.utils import navigate_to


def state_to_agent_obj(agent_data: Tuple):
    return AgentPlus(
        name=agent_data[0],
        prompt=agent_data[1],
        model=agent_data[2],
        code_execution=agent_data[3],
        chat_side=agent_data[4],
    )


def get_text_color(bg_color: str) -> str:
    """Calculate the luminance of the background color and return a suitable text color."""
    r, g, b = int(bg_color[1:3], 16), int(bg_color[3:5], 16), int(bg_color[5:7], 16)
    luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
    return 'white' if luminance < 0.5 else 'black'


def assign_agents_chat_colors(agents: List[Tuple]):
    updated_agents = []
    for agent in agents:
        random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        text_color = get_text_color(random_color)
        updated_agents.append((*agent, random_color, text_color))
    
    return updated_agents


def discussion_page():
    st.markdown("# AI Chat Battlefield")
    st.write("This is the stage where your configured agents will engage in the negotiation based on the setup parameters you've provided. Initiate the discussion and observe how the agents interact with each other to achieve the set goals.")

    if st.button("Kick Off Battle", key="start_conversation", type="primary", help="Start the discussion"):
        if not st.session_state.api_key:
            st.warning("Please enter your OpenAI API Key.", icon="⚠️")
            st.stop()
        
        if not st.session_state.manager_model:
            st.warning("Please select a preferred AI model.", icon="⚠️")
            st.stop()

        if len(st.session_state.agents) < 2:
            st.warning("A minimum of two agents are required to start the battle!", icon="⚠️")
            st.stop()

        st.session_state.agents = assign_agents_chat_colors(st.session_state.agents)
        agents = [state_to_agent_obj(agent_data) for agent_data in st.session_state.agents]
        discussion = GroupDiscussion(
            agents=agents, 
            extra_knowledge=st.session_state.knowledge, 
            human_feedback=st.session_state.human_feedback,
            model_name=st.session_state.manager_model,
            seed=st.session_state.seed,
        )
        user_proxy, manager = discussion.assemble_groupchat(num_rounds=st.session_state.num_rounds)
        message = f"{st.session_state.default_prompt}\n\n\n\n<Document context>\n\n{st.session_state.DOCUMENT}\n</Document context>\n\n\nBegin Discussion!" if st.session_state.DOCUMENT else f"{st.session_state.default_prompt}\n\n\nBegin Discussion!"
        user_proxy.initiate_chat(manager, message=message)

        st.button("Back to Setup Page", on_click=navigate_to, args=("setup",), type="secondary", help="Return to the setup page")
