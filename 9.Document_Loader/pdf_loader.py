from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('C:/Users/Harsh Verma/Desktop/Gen_AI_Using_Langchain/9.Document_Loader/dl-curriculum.pdf')

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[0].metadata)