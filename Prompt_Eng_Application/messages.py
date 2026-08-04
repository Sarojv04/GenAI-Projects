from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

messages_hist = = [

    SystemMessage(content = 'you are a helpfull assistance')
    HumanMessage(content = 'Tell me about langchain')
]
result = model.invoke(messages_hist)
messages_hist.append(AIMessage(content='result.content'))
print (messages_hist)