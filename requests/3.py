import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('../students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = '''
SELECT AVG(score), group_name
FROM score sc
	JOIN students st ON st.id=sc.student_id
	JOIN groups g ON g.id=st.group_id
GROUP BY g.id;
'''

print(execute_query(sql))
