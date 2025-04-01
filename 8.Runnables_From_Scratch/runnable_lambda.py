from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableLambda,RunnablePassthrough,RunnableParallel

load_dotenv()

def word_count(text):
    return len(text.split())


prompt = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=['topic']
)

model = ChatAnthropic(model='claude-3-5-sonnet-20241022')

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

parellel_chain = RunnableParallel({
    "joke" : RunnablePassthrough(),
    'word_count': RunnableLambda(word_count)
}) 

final_chain = RunnableSequence(joke_gen_chain, parellel_chain)

result= final_chain.invoke({'topic':'AI'})

final_result = """{}\n word count - {}""".format(result['joke'], result['word_count'])

print(final_result)