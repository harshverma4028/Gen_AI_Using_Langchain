from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from transformers import pipeline

text_gen_pipeline = pipeline(
    task="text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    temperature=0.5,
    max_new_tokens=100,
    do_sample=True,
    return_full_text=False 
)
llm = HuggingFacePipeline(pipeline=text_gen_pipeline)

result = llm.invoke("what is the capital of india")
print(result)
