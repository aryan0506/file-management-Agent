from fastapi import FastAPI
from pydantic import BaseModel
from main import agent
from logger import logger

class Prompt(BaseModel):
    prompt: str

app = FastAPI(title="File Management AI Agent API")

@app.post("/ask")
def ask(prompt:Prompt):
    logger.info(f"User asked: {prompt.prompt}")
    result = agent.run_sync(prompt.prompt)
    logger.info(f"Agent responded: {result.output}")
    return {"response": result.output}

@app.get("/tools")
def get_tools():
    logger.info("Tools requested")
    return {"tools": [tool.name for tool in agent.tools]}

@app.get("/logs")
def get_logs():
    logger.info("Logs requested")
    with open("logs/app.log", "r") as f:
        logs = f.read()
    return {"logs": logs}