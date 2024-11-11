from fastapi import FastAPI
from task import router as task_router
from user import router as user_router

router = APIRouter()

@router.get("/", response_model=list)
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.execute(select(User)).scalars().all()
    return users

@router.get("/user/{user_id}", response_model=User)
async def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.execute(select(User).where(User.id == user_id)).scalars().first()
    if user:
        return user
    raise HTTPException(status_code=404, detail="User was not found")

@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(user_data: CreateUser, db: Annotated[Session, Depends(get_db)]):
    new_user = User(**user_data.dict())
    db.add(new_user)
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}

@router.put("/update/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(user_id: int, user_data: UpdateUser, db: Annotated[Session, Depends(get_db)]):
    user_query = db.execute(select(User).where(User.id == user_id)).scalars().first()
    if user_query:
        for key, value in user_data.dict().items():
            setattr(user_query, key, value)
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}
    raise HTTPException(status_code=404, detail="User was not found")

@router.delete("/delete/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    user_query = db.execute(select(User).where(User.id == user_id)).scalars().first()
    if user_query:
        db.delete(user_query)
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'User deletion is successful!'}
    raise HTTPException(status_code=404, detail="User was not found")
