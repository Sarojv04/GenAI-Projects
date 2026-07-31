# Research Paper Summarizer 📄

I built this because reading research papers is painful. 
You spend hours on one paper and still don't fully get it.

This tool lets you choose HOW you want it explained — 
beginner friendly, technical, code oriented or mathematical. 
You also pick the language and format. The AI does the rest.

👉 Try it here: https://genai-projects-th2kwiupr69aywvbfq8e4z.streamlit.app/

## What it does

- Pick a research paper from the list
- Choose how you want it explained
- Choose the length, language and output format
- Hit summarize and get your answer

That's it. No complicated setup, just select and go.

## What I used to build it

- HuggingFace — the AI brain (Qwen2.5-72B)
- LangChain — to engineer the prompts dynamically
- Streamlit — to build the UI
- Python — everything runs on this

## How to run it locally

1. Clone this repo
2. Install dependencies
pip install -r requirements.txt
3. Add your HuggingFace API key in a .env file
HUGGINGFACEHUB_API_TOKEN=your_key_here
4. Run it
streamlit run Prompt_Eng_Application/pmt_Eng_App.py

## What I learned

Dynamic prompt engineering is powerful. Same paper, 
completely different output just by changing the prompt 
structure. That was the most interesting part of building this.

------------------- Next APP--------------------------------

## 🚀 Live App

Try it here: [Prompt Engineering Summary Tool](https://genai-projects-ztbuvl7rugifkwg5nip4ya.streamlit.app/)

Enter a prompt and get a quick AI-generated summary — powered by Hugging Face models via LangChain and deployed on Streamlit Community Cloud.

Still learning — feedback is always welcome! 🙌
structure. That was the most interesting part of building this.

Still learning — feedback is always welcome! 🙌
