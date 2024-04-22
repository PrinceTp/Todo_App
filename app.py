from fastapi import FastAPI
from . import models, schemas, services, database

app = FastAPI()

@app.post("/register")
async def register_user(user: schemas.User):
    return services.register_user(user)

@app.post("/login")
async def login_user(user: schemas.User):
    return services.login_user(user)

@app.get("/me")
async def get_current_user():
    return services.get_current_user()

@app.post("/todos")
async def create_todo_item(todo_item: schemas.TodoItem):
    return services.create_todo_item(todo_item)

@app.get("/todos")
async def get_todos():
    return services.get_todos()

@app.get("/todos/{todo_id}")
async def get_todo_item(todo_id: int):
    return services.get_todo_item(todo_id)

@app.put("/todos/{todo_id}")
async def update_todo_item(todo_id: int, todo_item: schemas.TodoItem):
    return services.update_todo_item(todo_id, todo_item)

@app.delete("/todos/{todo_id}")
async def delete_todo_item(todo_id: int):
    return services.delete_todo_item(todo_id)