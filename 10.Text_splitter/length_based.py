from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('C:/Users/Harsh Verma/Desktop/Gen_AI_Using_Langchain/9.Document_Loader/dl-curriculum.pdf')

docs = loader.load()

text = """When a spherical non-rotating body of a critical radius collapses under its own gravitation under general relativity, theory suggests it will collapse to a single point. This is not the case with a rotating black hole (a Kerr black hole). With a fluid rotating body, its distribution of mass is not spherical (it shows an equatorial bulge), and it has angular momentum. Since a point cannot support rotation or angular momentum in classical physics (general relativity being a classical theory), the minimal shape of the singularity that can support these properties is instead a ring with zero thickness but non-zero radius, and this is referred to as a ringularity or Kerr singularity."""

spliter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

spliter2= RecursiveCharacterTextSplitter(
    chunk_size= 100,
    chunk_overlap= 0,
)

reuslt = spliter2.split_text(text)

print(reuslt)