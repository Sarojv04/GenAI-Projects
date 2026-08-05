from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="conversational",
    max_new_tokens=512,
    temperature=0.1
)

#model = ChatHuggingFace(llm=llm, model_id="Qwen/Qwen2.5-7B-Instruct")
model = ChatHuggingFace(llm=llm)

chat_template = ChatPromptTemplate.from_messages(
    [
        ('system', 'You are a helpful AI assistant'),
        MessagesPlaceholder(variable_name='chat_history'),
        ('human', '{query}')
    ]
)

chat_history = []

with open('chat_history.txt', "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        if line.startswith("Human:"):
            chat_history.append(HumanMessage(content=line.replace("Human:", "").strip()))
        elif line.startswith("AI:"):
            chat_history.append(AIMessage(content=line.replace("AI:", "").strip()))

prompt = chat_template.invoke({'chat_history': chat_history, 'query': 'what is the amount?'})

print("\n========== Full Chat ==========")
print(prompt.to_string())


response = model.invoke(prompt)

print("\n========== AI Response ==========")
print(response.content)