import frontmatter
from pathlib import Path
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

def load_course_docs(course_dir="course_content"):
    docs = []
    for path in Path(course_dir).rglob("*.md"):
        post = frontmatter.load(path)
        docs.append(Document(
            page_content=post.content,
            metadata={
                "title": post.get("title", path.stem),
                "level": post.get("level", "unknown"),
                "order": post.get("order", 0),
                "source": str(path),
            }
        ))
    return docs

def build_index(course_dir="course_content", persist_dir="chroma_db"):
    docs = load_course_docs(course_dir)
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    chunks = splitter.split_documents(docs)
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = Chroma.from_documents(chunks, embeddings, persist_directory=persist_dir)
    print(f"Indexed {len(chunks)} chunks from {len(docs)} files.")
    return vectorstore

if __name__ == "__main__":
    build_index()
