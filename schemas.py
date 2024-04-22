from pydantic import BaseModel

class User(BaseModel):
    email: str
    password: str

class TodoItem(BaseModel):
    title: str
    description: str
    due_date: str