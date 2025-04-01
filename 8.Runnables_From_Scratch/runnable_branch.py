from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableLambda,RunnablePassthrough,RunnableParallel,RunnableBranch

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Sumarize the following text \n {text}",
    input_variables=['text']
)

model = ChatAnthropic(model='claude-3-5-sonnet-20241022')

parser = StrOutputParser()

report_gen_chain = RunnableSequence(prompt1 , model ,parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>100 , RunnableSequence(prompt2, model , parser)),
    RunnablePassthrough()
)

# final_chain = RunnableSequence(report_gen_chain ,branch_chain)
                     # LCEL Method
final_chain = report_gen_chain |branch_chain

print(final_chain.invoke({'topic':'Russia vs Ukraine'}))