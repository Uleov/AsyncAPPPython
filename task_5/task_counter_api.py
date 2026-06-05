from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import uuid

app = FastAPI(title="Счетчик задач")

tasks_db = {}

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1)

@app.post("/tasks", status_code=201)
async def create_task(task_input: TaskCreate):
    title = task_input.title.strip()
    if not title:
        raise HTTPException(status_code=400, detail="Ошибка пустое имя")
    
    task_id = str(uuid.uuid4())
    task = {"id": task_id, "title": title, "status": "created"}
    tasks_db[task_id] = task
    return task

@app.get("/tasks/{task_id}")
async def get_task(task_id: str):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Ошибка не найдено")
    return tasks_db[task_id]

@app.get("/tasks")
async def get_all_tasks():
    return list(tasks_db.values())

@app.patch("/tasks/{task_id}/done")
async def mark_task_done(task_id: str):
    if task_id not in tasks_db:
        raise HTTPException(status_code=404, detail="Ошибка не найдено")
    tasks_db[task_id]["status"] = "done"
    return tasks_db[task_id]
