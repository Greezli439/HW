import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('../students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = '''
SELECT AVG(score), students_name
    FROM score sc JOIN students s ON sc.student_id=s.id
    GROUP BY students_name 
    ORDER BY AVG(score) DESC
    LIMIT 5;
'''

print(execute_query(sql))
