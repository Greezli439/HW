import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('../students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = '''
SELECT students_name, score, discipline_name, group_name
FROM students st
    JOIN groups gr ON st.group_id=gr.id
	JOIN score sc ON sc.student_id=st.id
	JOIN disciplines ds ON ds.id=sc.discipline_id
WHERE group_name=112 AND discipline_name='physics'
ORDER BY students_name;
'''

print(execute_query(sql))
