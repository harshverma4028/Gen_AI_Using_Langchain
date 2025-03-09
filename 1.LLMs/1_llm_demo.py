from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')

result = llm.invoke("what is the capital of india")
print(result)













# from ai import streamText
# from ai_sdk.openai import createOpenAI
# from instructions import CHAT_INSTRUCTIONS

# # Set token, endpoint, and model name (free model setup)
# token deleted due to commit issue
# endpoint = "https://models.inference.ai.azure.com"
# modelName = "gpt-4o"

# # Function to invoke the model
# def invoke_model(prompt):
#     llm = createOpenAI(api_key=token, base_url=endpoint, model=modelName)
#     response = llm.invoke(prompt)
#     return response

# # Example usage
# result = invoke_model("What is the capital of India?")
# print(result)
