import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('../students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = '''
SELECT students_name, score, discipline_name, group_name, date_of
from students st
    JOIN groups gr ON gr.id=st.group_id
	JOIN score sc ON st.id=sc.student_id
	JOIN disciplines ds ON ds.id-sc.discipline_id
WHERE discipline_name='math' AND group_name='111' AND date_of = (
		SELECT date_of
		FROM score
		ORDER BY date_of DESC
		LIMIT 1)
;
'''

print(execute_query(sql))
