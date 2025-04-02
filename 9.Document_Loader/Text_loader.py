from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

prompt = PromptTemplate(
    template="wirte a summary for the following poem - \n {poem}",
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader('C:/Users/Harsh Verma/Desktop/Gen_AI_Using_Langchain/9.Document_Loader/cricket.txt', encoding='UTF-8')

docs = loader.load()

# print(docs[0])

# print(docs[0].page_content)
# print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({"poem":docs[0].page_content}))