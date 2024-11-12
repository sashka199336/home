# app/models/user.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db import Base
from .task import Task
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated
from models import User
from schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify

@router.get("/{user_id}/tasks")
def tasks_by_user_id(user_id: int):
    tasks = db.query(Task).filter(Task.user_id == user_id).all()
    return tasks
@router.delete("/delete")
def delete_user(user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Удаление связанных задач
    db.query(Task).filter(Task.user_id == user_id).delete()
    
    db.delete(user)
    db.commit()
    return {"status_code": status.HTTP_204_NO_CONTENT, "transaction": "Successful"}
    
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    tasks = relationship("Task", back_populates="user")
