import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('../students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = '''
SELECT students_name, lecturer_name, ROUND(AVG(score), 2)
from students st
	JOIN score sc ON st.id=sc.student_id
	JOIN disciplines ds ON ds.id=sc.discipline_id
	JOIN lecturers le ON le.id=ds.lecturer_id
WHERE students_name='David Johnson' AND lecturer_name='Jillian Warner' 
GROUP BY  lecturer_name, students_name
;


'''

print(execute_query(sql))
