from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='C:\\Users\\Harsh Verma\\Desktop\\Gen_AI_Using_Langchain\\9.Document_Loader\\books'
,
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()


# print(docs)
# print(docs[0].page_content)
# print(docs[0].metadata)

for document in docs:
    print(document.metadata)