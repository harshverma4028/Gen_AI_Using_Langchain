from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel, RunnablePassthrough


load_dotenv()

passthrough = RunnablePassthrough()

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

parser = StrOutputParser()


joke_gen_chain = RunnableSequence(prompt1, model, parser)

parellel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    "explanaion": RunnableSequence(prompt2 , model, parser)
})

final_chain = RunnableSequence(joke_gen_chain, parellel_chain)

result = final_chain.invoke({"topic":"cricket"})

print(result)