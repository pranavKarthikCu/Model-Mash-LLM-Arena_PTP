from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from rag_pipeline import load_rag_chain

app = FastAPI()
qa = load_rag_chain()  # Load Gemini-powered RAG chain at startup

# Allow CORS from React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify React's port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    question = data.get("question", "")

    if not question:
        return {"error": "No question provided."}

    response = qa.invoke(question)
    return {"answer": response['result']}