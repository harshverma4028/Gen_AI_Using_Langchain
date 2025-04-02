from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='full path.csv')

data = loader.load()

print(data[0])