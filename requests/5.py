import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('../students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = '''
SELECT discipline_name, lecturer_name
FROM disciplines d
	JOIN lecturers l ON l.id=d.lecturer_id;
'''

print(execute_query(sql))
