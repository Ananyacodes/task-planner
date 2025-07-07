from typing import TypedDict
from langgraph.graph import StateGraph, END
from model import generate_text


# Define the structure of the state passed between nodes
class AgentState(TypedDict):
    task: str
    plan: str
    result: str


# 🧠 Step 1: Planning Agent
def planner_agent(state: AgentState) -> AgentState:
    task = state["task"]
    prompt = f"Plan the following task:\n\n{task}"
    plan = generate_text(prompt)
    
    print("\n[Planner Agent]")
    print(f"Prompt:\n{prompt}")
    print(f"Generated Plan:\n{plan}\n")
    
    return {**state, "plan": plan}


# ⚙️ Step 2: Execution Agent
def executor_agent(state: AgentState) -> AgentState:
    plan = state["plan"]
    prompt = f"Execute this plan:\n\n{plan}"
    result = generate_text(prompt)

    print("\n[Executor Agent]")
    print(f"Prompt:\n{prompt}")
    print(f"Execution Result:\n{result}\n")
    
    return {**state, "result": result}


# 🔁 Build LangGraph flow
def create_agent_graph():
    builder = StateGraph(AgentState)
    
    builder.add_node("planner", planner_agent)
    builder.add_node("executor", executor_agent)
    
    builder.set_entry_point("planner")
    builder.add_edge("planner", "executor")
    builder.add_edge("executor", END)
    
    return builder.compile()
