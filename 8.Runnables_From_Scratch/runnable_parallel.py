from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel

load_dotenv()
model1 = ChatGoogleGenerativeAI(model='gemini-1.5-pro')

load_dotenv()
model2 = ChatAnthropic(model='claude-3-5-sonnet-20241022')


prompt1 = PromptTemplate(
    template="Generate a tweet about {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Generate a Linkedin post about {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "tweet": RunnableSequence(prompt1, model1 ,parser),
    "linkedin":RunnableSequence(prompt2, model2, parser)
})

print(parallel_chain.invoke({'topic':"AI"}))