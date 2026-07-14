"""
RAG chain for the Python Tutor chatbot.

Combines:
  - Static knowledge: retrieved course_content chunks (via Chroma)
  - Live state: current code pane text + current output/error text
    (NOT embedded — injected directly since it changes every keystroke)
"""

from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings, ChatOllama

CHROMA_DIR = "chroma_db"
EMBED_MODEL = "nomic-embed-text"
CHAT_MODEL = "qwen2.5:3b"

_vectorstore = None
_retriever = None
_llm = None


def _init():
    """Lazy-init so importing this module doesn't immediately hit Ollama."""
    global _vectorstore, _retriever, _llm
    if _llm is None:
        _vectorstore = Chroma(
            persist_directory=CHROMA_DIR,
            embedding_function=OllamaEmbeddings(model=EMBED_MODEL),
        )
        _retriever = _vectorstore.as_retriever(search_kwargs={"k": 2})
        _llm = ChatOllama(
            model=CHAT_MODEL,
            temperature=0,
            num_predict=200,
            keep_alive="1h",
        )
    return _retriever, _llm


PROMPT_TEMPLATE = """You are a concise Python tutor helping a student.

Current topic: {current_topic}

Relevant course material:
{course_context}

Student's current code:
```python
{code_pane}
```

Program output/error:
{output_pane}

Student's question: {question}

Answer directly and briefly. Reference their actual code or output if relevant.
"""


def answer_query(question: str, current_topic: str = "", code_pane: str = "", output_pane: str = "") -> str:
    """Main entry point called by the chat pane."""
    retriever, llm = _init()

    chunks = retriever.invoke(question)
    course_context = "\n\n".join(d.page_content for d in chunks) if chunks else "(no matching course material found)"

    prompt = PROMPT_TEMPLATE.format(
        current_topic=current_topic or "(none selected)",
        course_context=course_context,
        code_pane=code_pane or "(empty)",
        output_pane=output_pane or "(no output yet)",
        question=question,
    )

    response = llm.invoke(prompt)
    return response.content


if __name__ == "__main__":
    # Quick standalone smoke test
    print(answer_query("What is a decorator in Python?"))
