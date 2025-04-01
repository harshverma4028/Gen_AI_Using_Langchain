from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic']
)

model = ChatAnthropic(model='claude-3-5-sonnet-20241022')

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template="explain the following joke- {text}",
    input_variables=['text']
)

chain =  RunnableSequence(prompt1 , model, parser , prompt2, model, parser)

print(chain.invoke({'topic':"AI"}))