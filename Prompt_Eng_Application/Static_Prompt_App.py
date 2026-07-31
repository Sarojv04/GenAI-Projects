from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate
import os

#load_dotenv()

try:
    HUGGINGFACEHUB_API_TOKEN = st.secrets["HUGGINGFACEHUB_API_TOKEN"]
except (FileNotFoundError, KeyError, st.errors.StreamlitSecretNotFoundError):
    HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN", "")

os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN

st.header("Summary Tool")
user_input = st.text_input("Enter your prompt")

if st.button('Summarize'):
    if not user_input:
        st.warning("Please enter a prompt first.")
    elif not HUGGINGFACEHUB_API_TOKEN:
        st.error("HUGGINGFACEHUB_API_TOKEN not found. Please set it in .env or .streamlit/secrets.toml")
    else:
        with st.spinner("Generating summary..."):
            llm = HuggingFaceEndpoint(
                repo_id="Qwen/Qwen2.5-72B-Instruct",
                task="text-generation"
            )
            model = ChatHuggingFace(llm=llm)
            result = model.invoke(user_input)
            st.write(result.content)