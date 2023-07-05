from sqlalchemy import Column, Integer, String, ForeignKey, DATE
from sqlalchemy.orm import relationship
from database.db_connection import Base


class Group(Base):

    __tablename__ = 'Groups'
    id = Column(Integer, primary_key=True, autoincrement=True)
    group_name = Column(String(5), nullable=False)
    # student = relationship('Student', back_populates='Scores')


class Student(Base):

    __tablename__ = 'Students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_name = Column(String(30), nullable=False)
    group_id = Column(Integer, ForeignKey('Groups.id'))
    # group = relationship('Group')


class Lecturer(Base):

    __tablename__ = 'Lecturers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    lecturer_name = Column(String(30), nullable=False)
    # discipline = relationship('Discipline')


class Discipline(Base):

    __tablename__ = 'Disciplines'
    id = Column(Integer, primary_key=True, autoincrement=True)
    discipline_name = Column(String(15), nullable=False)
    lecturer_id = Column(Integer, ForeignKey('Lecturers.id'))
    # lecturer = relationship('Lecturer')
    # score = relationship('Score')


class Score(Base):

    __tablename__ = 'Scores'
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('Students.id'))
    student = relationship('Student', backref='Score')
    discipline_id = Column(Integer, ForeignKey('Disciplines.id'))
    discipline = relationship('Discipline', backref='Score')
    date = Column(DATE)
    score = Column(Integer)
