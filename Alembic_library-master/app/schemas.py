from pydantic import BaseModel

# Схемы для пользователей
class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int

class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: int

# Схемы для задач
class CreateTask(BaseModel):
    title: str
    content: str
    priority: int

class UpdateTask(BaseModel):
    title: str
    content: str
    priority: int
