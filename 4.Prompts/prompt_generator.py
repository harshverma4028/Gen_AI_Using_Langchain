from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
Please summarize the research titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}
Explanation Length :{length_input}
1. Mathematical Details:
    -Include relevant mathematical if present in the paper.
    -Explain the mathematical conceps using simple, intutive code snippets where
    applicable.
2. Analogies:
    - Use relatable analogies to simplify complex ideas.
If certain information is not available in the paper, respond with: "Insufficient 
information available" instead of guessing.
Ensure the summary is clear, accurate, and aligned with the provided style and length.
""",
input_varibles=['paper_input','style_input','length_input']
)

template.save('template.json')