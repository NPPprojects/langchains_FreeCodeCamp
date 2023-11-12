import langchain_helper as lch
import streamlit as st


st.title("Ask Wiki")

link = st.sidebar.text_input("Wiki article")
agent_command = st.sidebar.text_input("Your Question")


if link and agent_command:
    response = lch.langchain_agent(link,agent_command)
    st.markdown(response)