from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:12345@localhost/students'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()

DBSession = sessionmaker(bind=engine)
session = DBSession()
