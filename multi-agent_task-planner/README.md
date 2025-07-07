# 🧠 Multi-Agent Task Planner with Falcon LLM

![Streamlit Interface](https://img.shields.io/badge/UI-Streamlit-FF4B4B?logo=streamlit)
![HuggingFace](https://img.shields.io/badge/Model-Falcon--40B--instruct-yellow?logo=huggingface)
![LangChain](https://img.shields.io/badge/Framework-LangChain-blue)

An intelligent task decomposition system powered by Falcon-40B (with automatic fallback to Falcon-7B) that breaks complex goals into actionable subtasks using LangChain and LangGraph workflows.

---

## ✨ Features

- **Adaptive Model Loading**: Automatically switches between Falcon-40B and 7B based on available hardware  
- **Memory Optimization**: 4-bit quantization and efficient GPU memory management  
- **Professional Workflow**: LangGraph state management for reliable task decomposition  
- **Real-time Monitoring**: GPU memory tracking in the UI sidebar  
- **Fault Tolerance**: Comprehensive error handling with graceful degradation  

---

## 🛠️ Hardware Requirements

| Component   | Minimum Spec           | Recommended Spec         |
|-------------|------------------------|--------------------------|
| GPU         | RTX 3090 (24GB VRAM)   | A100/H100 (40GB+ VRAM)   |
| RAM         | 32GB                   | 64GB+                    |
| Storage     | 10GB (for 7B model)    | 80GB SSD (for 40B model) |

---

## 🚀 Quick Start

### Prerequisites

```bash
git clone https://github.com/your-repo/task-planner.git
cd task-planner
```

### Installation

Create and activate virtual environment:

```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
# OR
venv\Scripts\activate         # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

### Configuration

Create `.env` file for optional configurations:

```env
MODEL_SIZE=7b        # Force specific model (7b or 40b)
MAX_MEMORY=0.8       # Max GPU memory fraction to use
```

---

### Running the Application

```bash
streamlit run streamlit_app.py
```

---

## 📊 Performance Tips

**For consumer GPUs:**
- Set `MODEL_SIZE=7b` in `.env`
- Reduce `max_new_tokens` in `streamlit_app.py`

**For cloud deployments:**
- Enable `load_in_8bit=False` in `model.py` for better performance
- Increase `batch_size` in the pipeline setup
