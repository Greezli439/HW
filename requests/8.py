import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('../students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = '''
SELECT lecturer_name, AVG(score), discipline_name
FROM lecturers le
	JOIN disciplines ds ON ds.lecturer_id=le.id
	JOIN score sc ON sc.discipline_id=ds.id
GROUP BY discipline_name;
'''

print(execute_query(sql))
