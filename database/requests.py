from db_connection import session
from models import Lecturer, Student, Group, Discipline, Score
from sqlalchemy import func, desc, and_

request = ['Знайти 5 студентів із найбільшим середнім балом з усіх предметів.',
           'Знайти студента із найвищим середнім балом з певного предмета.'
           'Знайти середній бал у групах з певного предмета.',
           'Знайти середній бал на потоці (по всій таблиці оцінок).',
           'Знайти, які курси читає певний викладач.',
           'Знайти список студентів у певній групі.',
           'Знайти оцінки студентів в окремій групі з певного предмета.',
           'Знайти середній бал, який ставить певний викладач зі своїх предметів.',
           'Знайти список курсів, які відвідує певний студент.',
           'Список курсів, які певному студенту читає певний викладач.']


def select_one():
    result = session.query(Student.student_name, func.round(func.avg(Score.score), 2).label('avg_score'))\
        .select_from(Score)\
        .join(Student)\
        .group_by(Student.student_name)\
        .order_by(desc('avg_score'))\
        .limit(5).all()
    return result


def select_two(discipline_id):
    result = session.query(Student.student_name, Discipline.discipline_name, func.avg(Score.score).label('avg_score')) \
        .select_from(Score) \
        .join(Student) \
        .join(Discipline) \
        .filter(Discipline.id == discipline_id) \
        .group_by(Student.id, Discipline.discipline_name) \
        .order_by(desc('avg_score')) \
        .limit(1).all()
    return result


def select_three(discipline_id, group_id):
    result = session.query(Group.group_name, Discipline.discipline_name, func.avg(Score.score).label('avg_score')) \
        .select_from(Score) \
        .join(Student, Score.student_id == Student.id) \
        .join(Discipline, Score.discipline_id == Discipline.id) \
        .join(Group, Student.group_id == Group.id) \
        .filter(and_(Discipline.id == discipline_id, Group.id == group_id)) \
        .group_by(Group.group_name, Discipline.discipline_name) \
        .order_by(desc('avg_score')) \
        .all()
    return result


def select_four():
    result = session.query(func.avg(Score.score)).select_from(Score).all()
    return result


def select_five(teacher_id):
    result = session.query(Lecturer.lecturer_name, Discipline.discipline_name) \
        .select_from(Discipline) \
        .join(Lecturer, Discipline.lecturer_id == Lecturer.id) \
        .filter(Lecturer.id == teacher_id) \
        .order_by(Discipline.discipline_name) \
        .all()
    return result


def select_six(group_id):
    result = session.query(Student.student_name, Group.group_name) \
        .select_from(Student) \
        .join(Group) \
        .filter(Group.id == group_id) \
        .all()
    return result


def select_seven(group_id, discipline_id):
    result = session.query(Student.student_name, Score.score) \
        .select_from(Student) \
        .join(Score, Student.id == Score.student_id) \
        .join(Discipline, Score.discipline_id == Discipline.id) \
        .join(Group, Student.group_id == Group.id) \
        .filter(and_(Group.id == group_id, Discipline.id == discipline_id)) \
        .all()
    return result


def select_eight(lecturer_id):
    # discipline_id = (select(Discipline.id).join(Discipline) \
    #                  .join(Discipline, Discipline.lecturer_id == lecturer_id) \
    #                  .scalar_subquery())

    discipline_id = session.query(Discipline.id).select_from(Discipline) \
        .filter(Discipline.lecturer_id == lecturer_id).all()

    result = []

    for i in discipline_id:
        res = session.query(Discipline.discipline_name, func.avg(Score.score))\
            .select_from(Score) \
            .join(Discipline, Discipline.id == Score.discipline_id) \
            .join(Lecturer) \
            .filter(and_(Lecturer.id == lecturer_id, Discipline.id == i[0])) \
            .group_by(Discipline.discipline_name) \
            .all()
        result.append(res)
    return result


def select_nine(student_id):
    result = session.query(Discipline.discipline_name) \
        .select_from(Score) \
        .join(Discipline, Discipline.id == Score.discipline_id) \
        .join(Student, Student.id == Score.student_id) \
        .filter(Student.id == student_id) \
        .group_by(Discipline.discipline_name) \
        .all()
    return result


def select_ten(student_id, lecturer_id):
    result = session.query(Discipline.discipline_name) \
        .select_from(Score) \
        .join(Discipline) \
        .join(Lecturer) \
        .join(Student) \
        .filter(and_(Lecturer.id == lecturer_id, Student.id == student_id)) \
        .group_by(Discipline.discipline_name) \
        .all()
    return result


if __name__ == "__main__":
    result = [
        select_one(),
        select_two(2),
        select_three(4, 3),
        select_four(),
        select_five(2),
        select_six(1),
        select_seven(2, 1),
        select_eight(2),
        select_nine(12),
        select_ten(2, 3)
    ]

    for i, j in zip(request, result):
        print(i)
        print(j, end='\n\n')



