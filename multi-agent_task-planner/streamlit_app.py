import streamlit as st
from model import tokenizer, model
from transformers import pipeline
from langchain.prompts import PromptTemplate
from langchain_huggingface import HuggingFacePipeline
from langgraph.graph import StateGraph, END
from typing import TypedDict
import torch

# Setup UI
st.set_page_config(page_title="🧠 Multi-Agent Task Planner", layout="wide")
st.title("🧠 Multi-Agent Task Planner")

# Memory monitoring in sidebar
with st.sidebar:
    if torch.cuda.is_available():
        st.metric("GPU Memory", f"{torch.cuda.memory_allocated()/1e9:.2f}GB / {torch.cuda.get_device_properties(0).total_memory/1e9:.2f}GB")
    else:
        st.warning("Running on CPU - performance will be limited")

# Setup pipeline with error handling
@st.cache_resource(show_spinner=False)
def load_pipeline():
    try:
        return pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            max_new_tokens=150,
            temperature=0.7,
            top_p=0.9,
            repetition_penalty=1.1,
            device_map="auto",
            batch_size=1
        )
    except Exception as e:
        st.error(f"Failed to initialize pipeline: {str(e)}")
        st.stop()

hf_pipeline = load_pipeline()
llm = HuggingFacePipeline(pipeline=hf_pipeline)

# State management
class PlannerState(TypedDict):
    goal: str
    subtasks: list[str]

# Enhanced prompt template
prompt_template = """You are an expert project planner. Break this goal into clear, actionable steps:

Goal: {goal}

Considerations:
1. Prioritize logical sequence
2. Include dependencies
3. Make steps concrete and measurable

Subtasks:"""

prompt = PromptTemplate.from_template(prompt_template)

def task_planner(state: PlannerState) -> PlannerState:
    try:
        response = llm.invoke(prompt.format(goal=state["goal"]))
        return {"goal": state["goal"], "subtasks": response.strip().split("\n")}
    except Exception as e:
        st.error(f"Planning failed: {str(e)}")
        return {"goal": state["goal"], "subtasks": ["Error generating tasks"]}

# Build workflow graph
builder = StateGraph(PlannerState)
builder.add_node("plan_tasks", task_planner)
builder.set_entry_point("plan_tasks")
builder.add_edge("plan_tasks", END)
graph = builder.compile()

# Main UI
with st.form("task_planner"):
    user_goal = st.text_area("Enter your goal:", 
                           placeholder="Ex: 'Build a web app for customer feedback'",
                           height=100)
    
    if st.form_submit_button("Generate Subtasks", use_container_width=True):
        if not user_goal.strip():
            st.warning("Please enter a valid goal")
        else:
            with st.spinner("🧠 Planning tasks..."):
                try:
                    result = graph.invoke({"goal": user_goal})
                    st.subheader("✅ Action Plan")
                    
                    for i, task in enumerate(result["subtasks"], 1):
                        if task.strip():  # Skip empty lines
                            st.markdown(f"{i}. {task.strip()}")
                            
                except Exception as e:
                    st.error(f"Execution failed: {str(e)}")