import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('../students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = '''
SELECT students_name, lecturer_name, discipline_name
from students st
	JOIN score sc ON st.id=sc.student_id
	JOIN disciplines ds ON ds.id=sc.discipline_id
	JOIN lecturers le ON le.id=ds.lecturer_id
WHERE students_name='John Schneider' AND lecturer_name='Elizabeth Stein'
GROUP BY discipline_name
'''

print(execute_query(sql))
