from langchain_experimental.text_splitter import SemanticChunker
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

load_dotenv()

text_splitter = SemanticChunker(
    HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2'),breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1
)

sample = """
When a spherical non-rotating body of a critical radius collapses under its own gravitation under general relativity, theory suggests it will collapse to a single point. This is not the case with a rotating black hole (a Kerr black hole). With a fluid rotating body, its distribution of mass is not spherical (it shows an equatorial bulge), and it has angular momentum

As a part of the World Peace Conference that is going to be held on our campus from April 11th to 13th, we will also be having an Art Exhibition by our students.  Please share this information with your students and encourage them to bring their art for display, preferably poster art that can be hung/fixed on tapes/panels/frames either in the corridor of the Thiruvalluvar Block or in the corridor of the VMLS block around the Atrium.

"""
docs = text_splitter.create_documents([sample])

print(len(docs))
print(docs)