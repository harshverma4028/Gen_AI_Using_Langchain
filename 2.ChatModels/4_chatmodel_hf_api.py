from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = ""

llm = HuggingFaceEndpoint(
    repo_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("what is the capital of India")
print(result.content)

