import faker
from random import randint
from datetime import datetime, timedelta
from db_connection import session
from models import Student, Group, Lecturer, Discipline, Score

DISCIPLINES = ['math', 'physics', 'chemistry', 'ecology', 'history', 'geography']
GROUPS = [111, 112, 114]
COUNT_STUDENTS = 30
COUNT_LECTURERS = 4

fake_data = faker.Faker()


def generate_fake_data():
    lecturers, students = [], []

    for i in range(COUNT_STUDENTS):
        students.append(fake_data.name())
    for i in range(COUNT_LECTURERS):
        lecturers.append(fake_data.name())

    return lecturers, students

def select_random_group():
    return randint(1, len(GROUPS))


def fill_data_to_students(students_list):
    for student in students_list:
        new_record = Student(student_name=student, group_id=select_random_group())
        session.add(new_record)
    session.commit()


def fill_data_to_groups(groups_list):
    for i in groups_list:
        new_record = Group(group_name=i)
        session.add(new_record)
    session.commit()


def fill_data_to_lecturers(lecturers_list):
    for lecturer in lecturers_list:
        new_record = Lecturer(lecturer_name=lecturer)
        session.add(new_record)
    session.commit()


def fill_data_to_disciplines(disciplines_list):
    for discipline in disciplines_list:
        new_record = Discipline(discipline_name=discipline, lecturer_id=randint(1, COUNT_LECTURERS))
        session.add(new_record)
    session.commit()


def get_random_date():
    return fake_data.date_between(datetime.today() - timedelta(days=365))


def get_random_score():
    return randint(50, 100)


def fill_data_to_score(students_list):
    for id_st, _ in enumerate(students_list):
        for _ in range(20):
            new_record = Score(student_id=id_st+1, discipline_id=randint(1, len(DISCIPLINES)),
                               date=get_random_date(), score=get_random_score())
            session.add(new_record)
    session.commit()


if __name__ == "__main__":
    lecturers_list, students_list = generate_fake_data()

    # fill_data_to_groups(GROUPS)
    # fill_data_to_lecturers(lecturers_list)
    # fill_data_to_disciplines(DISCIPLINES)
    # fill_data_to_students(students_list)
    fill_data_to_score(students_list)
