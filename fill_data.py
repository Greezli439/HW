import faker
from random import random, choice, randint
import sqlite3
from datetime import datetime, timedelta


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
    return  randint(1, len(GROUPS))


def fill_data_to_students(students_list):
    sql = '''
    INSERT INTO students (students_name, group_id) VALUES(?, ?);
    '''
    data_groups = [select_random_group() for i in range(COUNT_STUDENTS)]
    cur.executemany(sql, zip(students_list, data_groups))

def fill_data_to_groups(groups_list):
    sql = '''
        INSERT INTO groups(group_name) VALUES(?);
        '''
    cur.executemany(sql, zip(groups_list, ))


def fill_data_to_lecturers(lecturers_list):
    sql = '''
        INSERT INTO lecturers(lecturer_name) VALUES(?);
        '''
    cur.executemany(sql, zip(lecturers_list, ))


def fill_data_to_disciplines(disciplines_list):
    sql = '''
        INSERT INTO disciplines(discipline_name, lecturer_id) VALUES(?, ?);
        '''
    cur.executemany(sql, zip(disciplines_list, iter(randint(1, COUNT_LECTURERS) for _ in disciplines_list)))


def get_random_date():
    return fake_data.date_between(datetime.today() - timedelta(days=365))


def get_random_score():
    return randint(50, 100)


def fill_data_to_score():
    disciplines_data = [1] * 3 + [2] * 3 + [3] * 4 + [4] * 3 + [5] * 3 + [6] * 4
    for i in range(1, COUNT_STUDENTS+1):
        date_data = [get_random_date() for _ in range(20)]
        score_data = [get_random_score() for _ in range(20)]
        sql = '''
            INSERT INTO score(discipline_id, student_id, date_of, score) VALUES(?, ?, ?, ?);
            '''
        students_data = [i] * 20
        cur.executemany(sql, zip(disciplines_data, students_data, date_data, score_data))


if __name__ == "__main__":
    lecturers_list, students_list = generate_fake_data()
    connect = sqlite3.connect('students.db')
    cur = connect.cursor()
    fill_data_to_groups(GROUPS)
    fill_data_to_students(students_list)
    fill_data_to_lecturers(lecturers_list)
    fill_data_to_disciplines(DISCIPLINES)
    fill_data_to_score()
    connect.commit()

