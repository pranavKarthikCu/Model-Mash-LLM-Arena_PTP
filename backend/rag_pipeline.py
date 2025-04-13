# rag_pipeline.py

import os
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

def load_rag_chain():
    # Load vector database
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.load_local("vectorstore/college_faiss", embedding, allow_dangerous_deserialization=True)
    retriever = db.as_retriever(search_kwargs={"k": 2})

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro-001",  # DO NOT change this to gemini-1.0 or anything else
        temperature=0.5,
        max_output_tokens=256
    )

    # Short, instructional prompt
    QA_PROMPT = PromptTemplate(
        input_variables=["context", "question"],
        template="""
    You are a helpful academic advisor who supports college students with registration, financial aid, and general inquiries. You always explain things clearly and informatively.

Use the context below to provide a detailed and informative answer to the question. You will try to mention a contact details when answering their queries. You may elaborate with examples, explanations, or helpful steps if needed.
Include phone numbers, email addresses, URLs exactly as given in the context

Context:
{context}

Question: {question}
Answer: (1-2 sentences)
"""
    )

    # Build RetrievalQA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=False,
        chain_type_kwargs={"prompt": QA_PROMPT}
    )

    return qa_chain
