import langchain_helper as lch
import streamlit as st
import textwrap

st.title("Ask Youtube video")

with st.sidebar:
    with st.form(key = "my_form"):
        youtube_url = st.sidebar.text_area(
            label="Youtube Video URL",
            max_chars=1000
        )
        query = st.sidebar.text_area(
            label="Your Question", 
            key="query"
            )
        submit_button = st.form_submit_button(label="Submit")

if query and youtube_url:
    db = lch.create_vector_db_from_youtube_url(youtube_url)
    response, docs = lch.get_response_from_query(db,querry=query)
    print(docs)
    st.subheader("Answer: ")
    st.text(textwrap.fill(response,width = 80))

