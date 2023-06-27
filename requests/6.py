import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('../students.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = '''
SELECT students_name
FROM students st
    JOIN groups gr ON st.group_id=gr.id
WHERE group_name=112;
'''

print(execute_query(sql))
