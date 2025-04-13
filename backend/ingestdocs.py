# ingest_docs.py

import os
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def load_documents(folder_path):
    docs = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            loader = TextLoader(os.path.join(folder_path, filename))
            docs.extend(loader.load())
    return docs

def main():
    # Step 1: Load documents
    docs = load_documents("/Users/tejk/Documents/ProjectX/data/scraped_pages")

    # Step 2: Split into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    # Step 3: Embed the chunks
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Step 4: Store in FAISS
    vectorstore = FAISS.from_documents(chunks, embedding)
    vectorstore.save_local("vectorstore/college_faiss")

if __name__ == "__main__":
    main()
