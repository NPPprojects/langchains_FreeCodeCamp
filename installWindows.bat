@echo off
python -m venv .venv
call %~dp0.venv\Scripts\activate.bat
pip install langchain==0.0.303 openai==0.28.1 streamlit python-dotenv
