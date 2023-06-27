
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_name VARCHAR(3) UNIQUE NOT NULL
    );

DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    students_name VARCHAR(50) UNIQUE NOT NULL,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups (id)
    );

DROP TABLE IF EXISTS lecturers;
CREATE TABLE lecturers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    lecturer_name VARCHAR(50) UNIQUE NOT NULL
    );

DROP TABLE IF EXISTS disciplines;
CREATE TABLE disciplines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    discipline_name VARCHAR(20) UNIQUE NOT NULL,
    lecturer_id INTEGER,
    FOREIGN KEY (lecturer_id) REFERENCES lecturers (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
    );

DROP TABLE IF EXISTS score;
CREATE TABLE score (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    discipline_id VARCHAR(20)  NOT NULL,
    student_id VARCHAR(3)  NOT NULL,
    date_of DATE NOT NULL,
    score INTEGER NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students (id),
    FOREIGN KEY (discipline_id) REFERENCES disciplines (id)
      ON DELETE CASCADE
      ON UPDATE CASCADE
    );