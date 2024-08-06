from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from getpass import getpass
from tqdm import tqdm
from pinecone import Pinecone, ServerlessSpec

GOOGLE_API_KEY = getpass("Google API Key: ")
loader = CSVLoader(file_path=r"matches.csv")

pages = loader.load()
print(len(pages))
print(pages[3].page_content[0:250])

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 400,
    chunk_overlap = 40,
    length_function = len,
    is_separator_regex = False,
)

chunks = list(tqdm(text_splitter.split_documents(pages), desc="Splitting documents"))
print(chunks[0])

model_name = "BAAI/bge-small-en"
model_kwargs = {"device":"cpu"}
encode_kwargs = {"normalize_embeddings":True}
bge_embeddings = HuggingFaceBgeEmbeddings(
    model_name=model_name, model_kwargs=model_kwargs, encode_kwargs=encode_kwargs
)

chunk_texts = list(map(lambda d: d.page_content, chunks))
embeddings = []

for chunk in tqdm(chunk_texts, desc="Generating embeddings"):
    embed = bge_embeddings.embed_documents([chunk])
    embeddings.append(embed[0])# because it returns an array containing the array
print(embeddings[0])

text_embedding_pairs = zip(chunk_texts, embeddings)
db = FAISS.from_embeddings(text_embedding_pairs, bge_embeddings)

while True:
    query = input("Enter query: ")

    contexts = db.similarity_search(query, k=5)
    print(contexts)

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an expert at answering questions based on a context extracted from a document. The context extracted from the document is: {context}"),
            ("human", "{question}"),
        ]
    )
    llm = ChatGoogleGenerativeAI(
        google_api_key=GOOGLE_API_KEY,
        model='gemini-1.5-pro-latest',
        temperature=0.9
    )
    chain = prompt | llm
    response = chain.invoke({
        "context": '\n\n'.join(list(map(lambda c: c.page_content, contexts))),
        "question": query
    })
    print("")
    print(response.content)