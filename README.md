# 🧠 Autonomous Blog Generation Agent

An AI-powered blog generation system built using **LLMs and agentic workflows**. This project generates SEO-friendly blog titles, structured content, and supports multilingual translation using a modular pipeline.

---

## 🚀 Overview

This project demonstrates how to design an **agent-based content generation system** using modern LLM frameworks.

The system:

* Takes a **topic** as input
* Generates a **creative blog title**
* Produces **structured blog content**
* Translates content into multiple languages
* Uses **state-based orchestration** for workflow management

---

## 🏗️ Architecture

The system is built using a **node-based agent workflow**:

1. **Title Generation Node**
2. **Content Generation Node**
3. **Translation Node**
4. **Routing Logic (Language-based)**

Each node updates a shared **state (`BlogState`)** using partial updates.

---

## ⚙️ Technologies Used

* **Python 3.10+**
* **FastAPI** – Backend API framework
* **LangGraph** – Agent workflow orchestration
* **LangChain** – LLM abstractions and integrations
* **ChatGroq (via Groq API)** – High-speed LLM inference
* **Pydantic** – Data validation and schema enforcement
* **Uvicorn** – ASGI server for FastAPI

---

---
## ⚡ LLM Provider

This project uses **ChatGroq** (powered by Groq) instead of OpenAI.

**Why ChatGroq?**

* ⚡ Ultra-fast inference (low latency)
* 💰 Cost-efficient compared to traditional providers
* 🔄 Compatible with LangChain ecosystem
* 🚀 Ideal for real-time agent workflows

---

---

## 📂 Project Structure

```
.
├── src/
│   ├── graphs/
│   │   └── graph_builder.py
│   ├── llms/
│   │   └── groqllm.py
│   ├── nodes/
│   │   └── blog_node.py
│   ├── states/
│   │   └── blogstate.py
│   └── main.py
├── requirements.txt
└── README.md
```

---

## ▶️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/vivekchandan73/autonomous-blog-agent.git
cd autonomous-blog-agent
```

---

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Set environment variables

```bash
set LANGCHAIN_PROJECT=your_project_name
set LANGCHAIN_API_KEY=your_api_key
set GROQ_API_KEY=your_api_key
```

---

### 5. Run the application

```bash
uvicorn app:app --reload
```

---

### 6. Access API

```
http://127.0.0.1:8000/docs
```

---

## 📌 Features

* ✅ SEO-friendly blog title generation
* ✅ Structured content creation (Markdown supported)
* ✅ Multilingual translation (Hindi, French, etc.)
* ✅ Modular agent-based workflow
* ✅ State management using LangGraph
* ✅ Scalable design for future extensions

---

## ⚠️ Challenges Faced & Solutions

### 1. ❌ LLM Structured Output Failure

**Issue:**
While generating long blog content, the system failed with:

```
tool_use_failed / invalid JSON / function call failure
```

**Root Cause:**

* LLM output exceeded token limits
* JSON response got truncated
* Schema validation failed

**Solution:**

* Limited blog generation to **<200 words**
* Reduced output size to maintain JSON integrity
* Ensured structured output reliability

---

### 2. ❌ Inconsistent Structured Output

**Issue:**
LLM sometimes failed to follow strict schema (`Blog` model)

**Solution:**

* Used `with_structured_output()` carefully
* Reduced complexity of prompts
* Avoided large structured responses

---

### 3. ❌ State Handling Confusion (LangGraph)

**Issue:**
Concern about losing state keys during updates

**Solution:**

* Understood that LangGraph uses **partial state updates (merge)**
* Only updated required fields (e.g., `blog`)
* Preserved other keys like `topic` automatically

---

### 4. ❌ Port Already in Use (FastAPI)

**Issue:**
Server failed to start due to port conflicts

**Solution:**

```bash
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

---

## 🧠 Key Learnings

* LLMs are **not reliable for large structured JSON outputs**
* Agent workflows require **careful state management**
* Breaking tasks into **smaller steps improves reliability**
* Token limits significantly impact system stability
* Structured output works best for **small, controlled responses**

---

## 🔮 Future Improvements

* ✨ Chunk-based blog generation (section-wise)
* ✨ Add database (MongoDB/PostgreSQL)
* ✨ UI dashboard using React
* ✨ Support more languages
* ✨ Add retry & guardrails for LLM failures
* ✨ Deploy using Docker & AWS

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a PR.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Vivek Chandan**
Python Developer | AI/ML Enthusiast

---
