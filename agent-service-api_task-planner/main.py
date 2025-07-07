from fastapi import FastAPI
from pydantic import BaseModel
from agent import create_agent_graph

# Initialize FastAPI app
app = FastAPI()

# Build the LangGraph agent graph
graph = create_agent_graph()

# Define request schema
class TaskRequest(BaseModel):
    task: str

# Define response endpoint
@app.post("/plan")
async def generate_plan(request: TaskRequest):
    try:
        result = graph.invoke({"task": request.task})
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}
