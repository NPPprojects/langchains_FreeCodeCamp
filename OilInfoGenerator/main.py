import langchain_helper as lch
import streamlit as st


st.title("Oil info generator")

oil_type = st.sidebar.text_input("What is your oil?")
info_amount = st.sidebar.number_input("Number of properties",min_value=1,max_value=10,step=1)


if oil_type and info_amount:
    response = lch.generate_oil_info(oil_type=oil_type, count=info_amount)
    st.markdown(response["output"])