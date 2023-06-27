import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('../students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = '''
SELECT AVG(score), students_name, discipline_name
    FROM score sc 
	JOIN students s ON sc.student_id=s.id
	JOIN disciplines d ON sc.discipline_id=d.id
    WHERE discipline_id = 1
    GROUP BY student_id
	ORDER BY AVG(score) DESC
    LIMIT 1;
'''

print(execute_query(sql))
