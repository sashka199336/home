# app/models/user.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db import Base
from .task import Task

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    firstname = Column(String, index=True)
    lastname = Column(String, index=True)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    tasks = relationship("Task", back_populates="user")
