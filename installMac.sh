#!/bin/bash
python3 -m venv .venv
source .venv/bin/activate
pip install langchain==0.0.303 openai==0.28.1 streamlit python-dotenv
