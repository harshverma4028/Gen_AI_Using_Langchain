from langchain_anthropic import ChatAnthropic

from langchain_huggingface import ChatHuggingFace ,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import JsonOutputParser


load_dotenv()

model = ChatAnthropic(model='claude-3-5-sonnet-20241022')

parser = JsonOutputParser()


template = PromptTemplate(
    template='Give me the name , age and city of a fictional person \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser 

result = chain.invoke({})

print(result)

