from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings, ChatOllama

vectorstore = Chroma(persist_directory="chroma_db", embedding_function=OllamaEmbeddings(model="nomic-embed-text"))
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

llm = ChatOllama(model="qwen3.5:9b", temperature=0.3)

query = "What is a decorator in Python?"
chunks = retriever.invoke(query)
context = "\n\n".join(d.page_content for d in chunks)
resp = llm.invoke(f"Course context:\n{context}\n\nQuestion: {query}", think=False)
print(resp.content)
