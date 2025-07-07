# 🤖 Planner–Executor Agents with FastAPI + LangGraph

![API](https://img.shields.io/badge/API-FastAPI-009688?logo=fastapi)
![LangGraph](https://img.shields.io/badge/Flow-LangGraph-blue)
![Model](https://img.shields.io/badge/Model-Tiny--GPT2-lightgrey?logo=huggingface)

A lightweight multi-agent system built using LangGraph, FastAPI, and Transformers. It mimics human reasoning by separating planning and execution using two collaborative agents powered by a language model.

---

## ✨ Features

- 🧠 **Planner Agent**: Creates a step-by-step strategy for a given task  
- ⚙️ **Executor Agent**: Executes the planned strategy to simulate outcomes  
- 🚀 **FastAPI Endpoint**: Accessible via `/plan` POST request  
- 💻 **Lightweight Model**: Uses `sshleifer/tiny-gpt2` — fast and CPU-friendly  
- 🧩 **LangGraph**: Clean and modular multi-agent orchestration

---

## ⚙️ Tech Stack

- Python 3.10+
- FastAPI + Uvicorn
- LangGraph + LangChain
- HuggingFace Transformers

---


## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-repo/langgraph-fastapi-agents.git
cd langgraph-fastapi-agents
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the FastAPI server
```bash
uvicorn main:app --reload
```

The API will be live at:  
**http://localhost:8000/plan**

---

## 🧪 Example Usage

### Request (POST `/plan`)
```json
{
  "task": "Write a blog post about AI safety"
}
```

### Response
```json
{
  "result": {
    "task": "Write a blog post about AI safety",
    "plan": "...",    
    "result": "..."   
  }
}
```

---

## 📦 Model Info

| Model Name              | Source                  | VRAM Usage | Suitable For       |
|--------------------------|-------------------------|------------|---------------------|
| `sshleifer/tiny-gpt2`    | Hugging Face 🤗         | Very Low   | CPU environments    |

You can swap this with any other `AutoModelForCausalLM` model from Hugging Face, like `gpt2`, `falcon-7b-instruct`, or quantized models (modify `model.py`).

---

## 💡 Improvements

- Add memory/context sharing between agents  
- Swap in a larger model or OpenAI endpoint  
- Add validation and error handling for edge cases  
- Add a Streamlit or Swagger UI frontend

---

## 🚨 Common Issues
If you see import errors:
```bash
# Install in development mode
pip install -e .
# OR set Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)/api-service"

## 👤 Author

Made with 💻 by Ananya (https://github.com/Ananyacodes)

---

## 📜 License

This project is open source and licensed under the MIT License.
