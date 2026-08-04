from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatOpenAI(model='gpt-4')

user_input = st.text_input("Enter a text")

st.header("Research Tool")

if st.button("Submit"):
    result = model.invoke(user_input)
    st.write(result.content)