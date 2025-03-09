from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

text = "Delhi is the capital of india"
documets = [
    "my name is Harsh verma",
    "I am from India ",
    "My PIN code is 851204"
]
# vector = embedding.embed_query(text)
vector = embedding.embed_documents(documets)

print(str(vector))