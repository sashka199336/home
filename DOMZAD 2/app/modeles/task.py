# app/models/task.py
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base
from .user import User
from fastapi import APIRouter, HTTPException, status
from models import Task, User
from database import SessionLocal
from schemas import CreateTask, UpdateTask

router = APIRouter()
db = SessionLocal()

@router.get("/")
def all_tasks():
    tasks = db.query(Task).all()
    return tasks
@router.get("/{task_id}")
def task_by_id(task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
@router.post("/create")
def create_task(task: CreateTask, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User was not found")
    
    new_task = Task(
        title=task.title,
        content=task.content,
        priority=task.priority,
        user_id=user_id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}
@router.put("/update")
def update_task(task_id: int, task: UpdateTask):
    existing_task = db.query(Task).filter(Task.id == task_id).first()
    if not existing_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    existing_task.title = task.title
    existing_task.content = task.content
    existing_task.priority = task.priority
    db.commit()
    db.refresh(existing_task)
    return existing_task
@router.delete("/delete")
def delete_task(task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(task)
    db.commit()
    return {"status_code": status.HTTP_204_NO_CONTENT, "transaction": "Successful"}  
class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String, index=True)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    slug = Column(String, unique=True, index=True)

    user = relationship("User", back_populates="tasks")
