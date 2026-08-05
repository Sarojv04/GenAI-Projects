from langchain_core.prompts import ChatPromptTemplate
#from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

chat_template = ChatPromptTemplate([
                # SystemMessage(content='you are a knowledgable {domain} expert'),
                # HumanMessage(content = 'explain the {topic} in simple way with one example')
                ('system', 'you are a knowledgable {domain} expert'),
                ('user', 'explain the {topic} in simple way with one example')
])

prompt = chat_template.invoke({'domain' : 'bank',
                               'topic' : 'loan'})
print(prompt)
