# Corrected streamlit_app.py
import streamlit as st
from model import generate_text  # Will be resolved by proper structure
from agent import create_agent_graph

graph = create_agent_graph()

st.title("PlannerExecutor Agents")
task = st.text_area("Enter a task")

if st.button("Generate Plan and Execute"):  # Fixed colon
    if task.strip():
        result = graph.invoke({"task": task})
        st.subheader("Plan")
        st.write(result["plan"])  # Fixed missing parenthesis
        st.subheader("Execution Result")
        st.write(result["result"])