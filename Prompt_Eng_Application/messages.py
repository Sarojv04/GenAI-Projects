from langchain_openai import ChatOpenAI
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

#model = ChatOpenAI()

messages_hist = [
    SystemMessage(content = 'you are a helpfull assistance'),
    HumanMessage(content = 'Tell me about langchain')
    ]
result = model.invoke(messages_hist)
messages_hist.append(AIMessage(content='result.content'))
print (messages_hist)