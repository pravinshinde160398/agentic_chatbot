import streamlit as st

from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI


def load_langgraph_agenticai_app():
    """
    Summary
    """
    
    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()
    
    if not user_input:
        st.error("error")
        return
    
    user_message = st.chat_input("Enter msg")