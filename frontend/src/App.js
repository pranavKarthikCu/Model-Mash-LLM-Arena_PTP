import React, { useState, useEffect, useRef } from "react";

function App() {
  const [messages, setMessages] = useState([
    {
      sender: "bot",
      text: "👋 Hi! I'm Blaze, your UTA Chatbot. Ask me anything about schedules, timings, or events.",
    },
  ]);
  const [input, setInput] = useState("");
  const [isOpen, setIsOpen] = useState(false);
  const messagesEndRef = useRef(null);

  const handleSend = async () => {
    if (input.trim() === "") return;
  
    const userMessage = { sender: "user", text: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
  
    try {
      const res = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: input }),
      });
  
      const data = await res.json();
  
      const botReply = {
        sender: "bot",
        text: data.answer || "Sorry, I couldn't find an answer.",
      };
  
      setMessages((prev) => [...prev, botReply]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        { sender: "bot", text: "Error connecting to backend." },
      ]);
      console.error("Backend error:", error);
    }
  };
  

  const handleKeyPress = (e) => {
    if (e.key === "Enter") handleSend();
  };

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  return (
    <>
      {/* Floating Blaze button */}
      {!isOpen && (
        <img
          src="/blaze.png"
          alt="Open Chatbot"
          onClick={() => setIsOpen(true)}
          style={{
            position: "fixed",
            bottom: "20px",
            right: "20px",
            height: "60px",
            width: "60px",
            borderRadius: "50%",
            cursor: "pointer",
            transition: "transform 0.3s ease",
            boxShadow: "0 0 10px rgba(0, 0, 0, 0.2)",
          }}
          onMouseOver={(e) => (e.currentTarget.style.transform = "scale(1.1)")}
          onMouseOut={(e) => (e.currentTarget.style.transform = "scale(1.0)")}
        />
      )}

      {/* Centered chatbot modal */}
      {isOpen && (
        <div style={styles.overlay}>
          <div style={styles.chatBox}>
          <div style={styles.header}>
  <img src="/uta_logo.png" alt="UTA Logo" style={styles.logo} />
  <h2 style={styles.title}>Ask UTA</h2>
</div>

<button onClick={() => setIsOpen(false)} style={styles.closeBtn}>
  ✖
</button>

            
            <div style={styles.messages}>
              {messages.map((msg, idx) => (
                <div
                  key={idx}
                  style={{
                    ...styles.messageRow,
                    flexDirection:
                      msg.sender === "user" ? "row-reverse" : "row",
                  }}
                >
                  <img
                    src={
                      msg.sender === "bot"
                        ? "/blaze.png"
                        : "https://cdn-icons-png.flaticon.com/512/9131/9131529.png"
                    }
                    alt={`${msg.sender} avatar`}
                    style={styles.avatar}
                  />
                  <div
                    style={{
                      ...styles.messageBubble,
                      backgroundColor:
                        msg.sender === "user" ? "#F47C20" : "#e0e0e0",
                      color: msg.sender === "user" ? "white" : "black",
                      alignSelf:
                        msg.sender === "user" ? "flex-end" : "flex-start",
                    }}
                  >
                    {msg.text}
                  </div>
                </div>
              ))}
              <div ref={messagesEndRef} />
            </div>
            <div style={styles.inputBox}>
              <input
                type="text"
                placeholder="Type your message..."
                style={styles.input}
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={handleKeyPress}
              />
              <button onClick={handleSend} style={styles.button}>
                Send
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
}

const styles = {
  container: {
    height: "100vh",
    backgroundColor: "#f7f7f7",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
  },
  chatBox: {
    width: "420px",
    height: "600px",
    borderRadius: "10px",
    boxShadow: "0 0 15px rgba(0,0,0,0.1)",
    display: "flex",
    flexDirection: "column",
    backgroundColor: "#ffffff",
    overflow: "hidden",
    border: "3px solid #003366",
  },
  header: {
    backgroundColor: "#003366",
    color: "white",
    padding: "0.75rem 1rem",
    display: "flex",
    alignItems: "center",
    gap: "0.75rem",
  },
  logo: {
    height: "35px",
  },
  title: {
    margin: 0,
    fontSize: "1.3rem",
  },
  messages: {
    flex: 1,
    padding: "1rem",
    overflowY: "auto",
    display: "flex",
    flexDirection: "column",
    gap: "0.75rem",
  },
  messageRow: {
    display: "flex",
    alignItems: "flex-end",
    gap: "0.5rem",
  },
  avatar: {
    height: "40px",
    width: "40px",
    borderRadius: "50%",
    objectFit: "cover",
  },
  messageBubble: {
    padding: "0.6rem 1rem",
    borderRadius: "15px",
    maxWidth: "70%",
    fontSize: "0.95rem",
    lineHeight: "1.4",
  },
  inputBox: {
    display: "flex",
    borderTop: "1px solid #ccc",
  },
  overlay: {
    position: "fixed",
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    backgroundColor: "rgba(0, 0, 0, 0.5)",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    zIndex: 9999,
  },  
  input: {
    flex: 1,
    padding: "0.75rem",
    border: "none",
    outline: "none",
    fontSize: "1rem",
  },
  closeBtn: {
    position: "absolute",
    top: "10px",
    right: "10px",
    height: "32px",
    width: "32px",
    borderRadius: "50%",
    border: "none",
    backgroundColor: "#003366",
    color: "white",
    cursor: "pointer",
    fontSize: "16px",
    fontWeight: "bold",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    boxShadow: "0 0 6px rgba(0, 0, 0, 0.2)",
    transition: "transform 0.2s",
  },
  
  button: {
    padding: "0 1.5rem",
    backgroundColor: "#003366",
    color: "white",
    border: "none",
    cursor: "pointer",
    fontWeight: "bold",
  },
};

export default App;
