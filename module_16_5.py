from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List
from contextlib import asynccontextmanager

app = FastAPI()

# Подключаем шаблоны из папки 'templates'
templates = Jinja2Templates(directory="templates")

# Список пользователей
users: List['User'] = []

# Модель User
class User(BaseModel):
    id: int
    username: str
    age: int

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Инициализация при старте
    yield
    # Очистка ресурсов при завершении
    pass

app.router.lifespan = lifespan

# Маршрут для отображения всех пользователей с использованием шаблона
@app.get("/", response_class=HTMLResponse)
async def read_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users, "user": None})

# POST запрос для добавления нового пользователя
@app.post("/user/{username}/{age}", response_model=User)
async def create_user(username: str, age: int):
    user_id = users[-1].id + 1 if users else 1  # Увеличение id на 1 или 1 для первого пользователя
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user

# Измененный GET запрос для отображения информации о конкретном пользователе
@app.get("/users/{user_id}", response_class=HTMLResponse)
async def read_user(request: Request, user_id: int):
    user = next((user for user in users if user.id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User was not found")
    return templates.TemplateResponse("users.html", {"request": request, "users": users, "user": user})

# DELETE запрос для удаления пользователя
@app.delete("/user/{user_id}", response_model=User)
async def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(index)
            return deleted_user
    raise HTTPException(status_code=404, detail="User was not found")
