from langchain_openai import ChatOpenAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

template = PromptTemplate(
    template = 'write a detail report on the {topic}',
    input_variable = ['topic']
)

template1 = PromptTemplate(
    template = 'write five line summary on the following text. \n {text}',
    input_variable = ['text']
)

parser = StrOutputParser()

chain = template | model | parser | template1 | model | parser

result = chain.invoke({'topic' : 'AI'})

print(result)

