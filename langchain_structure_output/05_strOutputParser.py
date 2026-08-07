from langchain_openai import ChatOpenAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate



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

prompt1 = template.invoke({'topic' : 'AI'})
result = model.invoke(prompt1)

prompt2 = template1.invoke({'text' : result.content})

final_result = model.invoke(prompt2)

print(final_result.content)