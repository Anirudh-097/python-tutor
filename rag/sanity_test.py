from time import perf_counter

from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

# Initialize
t0 = perf_counter()

vectorstore = Chroma(
    persist_directory="chroma_db",
    embedding_function=OllamaEmbeddings(model="nomic-embed-text"),
)
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

llm = ChatOllama(
    model="qwen2.5:3b",
    temperature=0,
    num_predict=200,
    keep_alive="1h",
)

t1 = perf_counter()

query = "What is a decorator in Python?"

# Retrieve relevant chunks
chunks = retriever.invoke(query)
t2 = perf_counter()

# Build prompt
context = "\n\n".join(d.page_content for d in chunks)
messages = [
    SystemMessage(
        content=(
            "You are a Python tutor. "
            "Answer only using the supplied course context. "
            "Include one short Python example when appropriate."
        )
    ),
    HumanMessage(
        content=f"""Course context:
{context}

Question:
{query}
"""
    ),
]
t3 = perf_counter()

# Generate response
# resp = llm.invoke(prompt, think=False)
# print(resp.content)

for chunk in llm.stream(messages, think=False):
    print(chunk.content, end="", flush=True)

t4 = perf_counter()

print("\n=== Timing ===")
print(f"Initialization : {t1 - t0:.3f} s")
print(f"Retrieval      : {t2 - t1:.3f} s")
print(f"Prompt Build   : {t3 - t2:.3f} s")
print(f"LLM Generation : {t4 - t3:.3f} s")
print(f"Total          : {t4 - t0:.3f} s")

print("\n=== Misc ===")
print(f"Context length: {len(context)} characters")
print(f"Number of chunks: {len(chunks)}")
