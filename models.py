import datetime
from sqlalchemy import (Column, String, Integer, Text, Date, DateTime, Boolean, ForeignKey, create_engine)
from sqlalchemy.orm import Session, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///app.sqlite', echo=True)
Base = declarative_base(bind=engine)

class Abstract(Base):
    __abstract__= True
    id = Column(Integer, primary_key=True)
    created_on  = Column(DateTime, default=datetime.datetime.now())

class User(Abstract, Base):
    __tablename__ = 'users'
    name = Column(String(30), unique=True, nullable=False)
    email = Column(String(40), unique=True, nullable=False)
    password = Column(String(50), nullable=False)

    user_links = relationship('Link')

    def __str__(self):
        return ' | '.join([self.name, self.id, self.email, self.password])

class Task(Abstract, Base):
    __tablename__= 'tasks'
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String(40), unique=True, nullable=False)
    content = Column(String(300), nullable=False)
    url = Column(Text, nullable=False, unique=True)
    rating = Column(Integer, default=0)
    tags = Column(Text, nullable=False)

    author = relationship('User')

    def __str__(self):
        return ' | '.join([self.id, self.user_id, self.title, self.url])

Base.metadata.create_all()

