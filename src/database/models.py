from sqlalchemy.ext.declarative import declarative_base
from src.database.db import engine
from sqlalchemy import Column, Integer, String, func, Date, Boolean
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()

class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(15), nullable=False)
    last_name = Column(String(20))
    email = Column(String(50))
    phone = Column(String(13), unique=True)
    birthday = Column(Date)
    user_id = Column('user_id', ForeignKey('users.id', ondelete='CASCADE'), default=None)



class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column('created_at', DateTime, default=func.now())
    avatar = Column(String(255), nullable=True)
    refresh_token = Column(String(255))
    confirmed = Column(Boolean, default=False)


Base.metadata.create_all(bind=engine)
