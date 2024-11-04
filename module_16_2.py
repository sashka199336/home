from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

# Маршрут к страницам пользователей с параметром user_id
@app.get("/user/{user_id}")
async def read_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", examples=1)]):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

# Маршрут к страницам пользователей с параметрами username и age
@app.get("/user/{username}/{age}")
async def read_user_info(
    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", examples="UrbanUser")],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age", examples=24)]
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
