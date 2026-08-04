from langchain_core.prompts import PromptTemplate

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

""",
validation_tampalte = True
)

template.save('template.json')