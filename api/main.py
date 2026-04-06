from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json, os

app = FastAPI(title="Personaliza01 API", description="API para tarefas educacionais", version="1.0.0")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def root():
    return {"message": "Bem-vindo à API de Tarefas Educacionais!"}

@app.get("/assignments")
def get_assignments():
    config_path = os.path.join(os.path.dirname(__file__), "../config.json")
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
    return config

@app.get("/assignments/{assignment_id}")
def get_assignment(assignment_id: str):
    config_path = os.path.join(os.path.dirname(__file__), "../config.json")
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
    assignments = config.get("assignments", [])
    for a in assignments:
        if a.get("id") == assignment_id:
            return a
    return {"error": "Tarefa não encontrada"}, 404
