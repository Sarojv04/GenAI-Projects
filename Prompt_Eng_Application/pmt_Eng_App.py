from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

#load_dotenv()

import os

HUGGINGFACEHUB_API_TOKEN = st.secrets.get(
    "HUGGINGFACEHUB_API_TOKEN",
    os.getenv("HUGGINGFACEHUB_API_TOKEN", "")
)
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN

# ─────────────────────────────
# UI PART
# ─────────────────────────────
st.set_page_config(page_title="Research Tool", page_icon="📄", layout="centered")

st.markdown("""
    <style>
    .stSelectbox label { font-size: 13px; color: gray; }
    .stButton button { width: 100%; border-radius: 8px; padding: 10px; }
    </style>
""", unsafe_allow_html=True)

st.title("📄 Research Tool")
st.caption("Select a paper and customize your explanation")
st.divider()

paper_input = st.selectbox("📄 Research Paper", [
    "Attention Is All You Need",
    "BERT: Pre-training of Deep Bidirectional Transformers",
    "GPT-3: Language Models are Few-Shot Learners",
    "Diffusion Models Beat GANs on Image Synthesis",
    "ResNet: Deep Residual Learning for Image Recognition",
    "LLaMA: Open and Efficient Foundation Language Models",
])

col1, col2 = st.columns(2)

with col1:
    style_input = st.selectbox("🎨 Explanation Style",
        ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])

    language_input = st.selectbox("🌐 Language",
        ["English", "Hindi", "Spanish", "French"])

with col2:
    length_input = st.selectbox("📏 Length",
        ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])

    format_input = st.selectbox("📋 Output Format",
        ["Plain Text", "Bullet Points", "Summary + Key Takeaways", "Q&A Format"])

# ─────────────────────────────
# APPLICATION PART
# ─────────────────────────────
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

template = PromptTemplate(
    input_variables=["paper_input", "style_input", "length_input", "language_input", "format_input"],
    template="""
Please summarize the research paper titled "{paper_input}" with the following specifications:

Explanation Style: {style_input}
Explanation Length: {length_input}
Output Language: {language_input}
Output Format: {format_input}

1. Mathematical Details:
   - Include relevant mathematical equations if present in the paper.
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.

2. Analogies:
   - Use relatable analogies to simplify complex ideas.

3. Format Instructions:
   - If Output Format is "Bullet Points", respond in bullet points.
   - If Output Format is "Summary + Key Takeaways", provide a summary followed by key takeaways.
   - If Output Format is "Q&A Format", respond in question and answer format.
   - If Output Format is "Plain Text", respond in plain paragraph form.

4. Language Instructions:
   - Respond in {language_input} language only.

If certain information is not available in the paper, respond with: "Insufficient
information available" instead of guessing.

Ensure the summary is clear, accurate, and aligned with the provided style and length.
"""
)

# ─────────────────────────────
# BUTTON + RESULT
# ─────────────────────────────
if st.button("✨ Summarize"):
    with st.spinner("Generating summary..."):
        prompt = template.invoke({
            'paper_input': paper_input,
            'style_input': style_input,
            'length_input': length_input,
            'language_input': language_input,
            'format_input': format_input
        })
        result = model.invoke(prompt)

    st.divider()
    st.subheader("Result")
    st.caption(f"`{paper_input}` · `{style_input}` · `{language_input}` · `{length_input}`")
    st.info(result.content)