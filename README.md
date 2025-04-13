# Model-Mash-LLM-Arena_PTP

UTA Datathon 2025 Report
Team – PTP Codex
Project AskUTA
Datathon Report: AskUTA Chatbot
________________________________________

<img width="549" alt="Screenshot 2025-04-13 at 5 41 52 AM" src="https://github.com/user-attachments/assets/90cbae33-5f38-4dca-bf61-72c0f970b179" />


📅 Event
UTA Datathon 2025
🏛️ Project Title
AskUTA Chatbot
🎓 Team Name
PTPCodex
👥 Team Members
1.	Prajwal Mrithyunjay Hulamani – Student ID: 1002248365
2.	Pranav Karthik Chinya Umesha – Student ID: 1002238679
3.	Tejaswi Kulkarni
________________________________________
🔄 Introduction
The AskUTA Chatbot is a Large Language Model (LLM)-powered conversational assistant developed to enhance the campus experience at the University of Texas at Arlington (UTA). It is designed to answer questions related to university schedules, departments, events, and resources. The chatbot seamlessly integrates a custom LLM backend with a responsive React frontend.
Our goal was to develop a user-friendly, intelligent assistant that leverages the power of natural language processing to understand and respond to student queries in real-time, reducing the dependency on manual searches and support.
________________________________________
🔧 System Architecture
Overview
The system comprises three primary components:
1.	Frontend: Built with React.js, offering an intuitive chat interface.
2.	Backend: Connects the frontend with our LLM using a lightweight Node.js or Python-based server.
3.	LLM Model: A custom fine-tuned large language model hosted locally or via an API.
Architecture Diagram
User → React Frontend → Backend Server → LLM Model → Response → Frontend
________________________________________
🛍️ Tech Stack
•	Frontend: React.js, HTML/CSS, JavaScript
•	Backend: Node.js / FastAPI
•	LLM Model: Custom-trained LLM using open-source base models
•	Hosting: Netlify (frontend)
________________________________________
📈 Key Features
•	Natural conversation interface
•	Instant response from local LLM
•	Easy deployment using Netlify
•	Fully customizable and scalable
________________________________________
⚙️ Development Process
🔧 Development Process
The development of our custom chatbot involved several distinct phases, each contributing to a robust and responsive system built around our custom knowledge base and LLM integration.
________________________________________
1.	Data Collection and Preprocessing
We began by collecting relevant information from the University of Texas at Arlington (UTA) website. This involved:
•	Web scraping using BeautifulSoup to extract structured text data from various web pages.
•	Performing text cleaning and formatting to prepare the data for embedding.
•	Removing unnecessary HTML tags, scripts, and duplicate content to ensure relevance and accuracy.
________________________________________
2.	Document Ingestion and Embedding
Once the raw text was cleaned:
•	We used LangChain and Hugging Face Transformers to load the textual data and split it into manageable chunks.
•	These chunks were transformed into high-dimensional embeddings using a pre-trained sentence transformer model.
•	The resulting vectors were stored in a FAISS vector store, enabling fast and accurate similarity searches.
________________________________________
3. LLM Integration and Prompt Engineering
We used Gemini, a state-of-the-art large language model (LLM), to generate responses based on retrieved knowledge. Our pipeline follows a Retrieval-Augmented Generation (RAG) approach:
•	User Query → Embedding → Similarity Search in FAISS
•	Retrieved document chunks were combined into a structured prompt, which was passed to the Gemini model.
•	The prompt format ensured context retention, enabling Gemini to generate domain-specific, coherent responses.
________________________________________
4. Frontend Development
The chatbot’s interface was built using React:
•	A simple and intuitive chat UI was created using state management hooks.
•	User messages were captured, displayed, and passed to the backend.
•	The LLM's response was then displayed in the UI with real-time rendering and scroll handling using useRef.
________________________________________
5. Backend Integration
The backend handled:
•	Receiving user input and converting it to embeddings.
•	Querying FAISS for the top-k most relevant document chunks.
•	Constructing a prompt with retrieved context.
•	Sending the prompt to Gemini and returning the model’s response to the frontend.
________________________________________
6. Deployment
•	The frontend was deployed using Netlify, offering free hosting and easy integration with GitHub.
•	The backend and FAISS server (if used externally) were hosted separately or run locally during development.
•	Environment variables were managed to separate local vs. production endpoints.
________________________________________
❌ Challenges Faced
•	PowerShell script restrictions when installing packages (resolved by setting execution policies)
•	Model latency during local execution
•	CORS issues while connecting frontend to backend
•	Optimizing prompt engineering for better answers
________________________________________
✨ Highlights & Impact
•	Helps students get real-time information on campus queries
•	Can be expanded to include RAG (retrieval-augmented generation)
•	Fully local model allows offline and private data handling
________________________________________
🔄 Future Scope
•	Integrate vector database (e.g., FAISS) for memory/context
•	Deploy backend on cloud for wider access
•	Add speech-to-text and multi-language support
•	Integrate calendar APIs for event lookups
________________________________________
📄 Conclusion
The AskUTA Chatbot demonstrates how LLMs can revolutionize campus engagement through automation and intelligent assistance. Our team successfully built a working prototype that can be scaled and enhanced for production use at UTA.
We believe this chatbot can evolve into a core part of UTA’s digital ecosystem, making university life more accessible, efficient, and engaging for students and staff alike.
________________________________________
Submitted by Team PTPCodex for UTA Datathon 2025

