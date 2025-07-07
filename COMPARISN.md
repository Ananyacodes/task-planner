# AI Planning Systems Comparison

## 🏗️ Architectural Overview
| Component          | API Service (`/agent-service-api`) | Multi-Agent UI (`/multi-agent-ui`) |
|--------------------|------------------------------------|------------------------------------|
| **Type**           | Microservice (Backend)             | Interactive App (Frontend)         |
| **Framework**      | FastAPI                            | Streamlit                          |
| **Model**          | Tiny-GPT2 (CPU)                    | Falcon-40B/7B (GPU)                |
| **Workflow**       | LangGraph Agents                   | Linear Execution                   |
| **Input**          | REST API Calls                     | Web UI Forms                       |

## ⚙️ Technical Specifications
### API Service
```python
# Key Characteristics
- Latency: 200-500ms (CPU-bound)
- Scalability: Horizontal (container-ready)
- Dependencies: FastAPI, Pydantic, Uvicorn

🛠️ Development Experience
# API Service Pros
✅ Easier debugging (structured logs)
✅ CI/CD friendly
✅ Lightweight dependencies

# Multi-Agent UI Pros
✅ Visual feedback
✅ Rapid prototyping
✅ Built-in caching

🚀 Deployment Scenarios
# Choose API Service When:

Need API integration
Running on edge devices
Require high availability

# Choose Multi-Agent UI When:

Demo/POC needed
GPU resources available
Interactive debugging