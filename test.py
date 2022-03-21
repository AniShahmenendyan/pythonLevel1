import psycopg2

conn = psycopg2.connect("dbname=python_level1 user=postgres password=pass host=127.0.0.1")
#
cur = conn.cursor()

# try:
cur.execute('select * from users')

# print(cur.fetchone())
# print(cur.fetchone())
# print(cur.fetchall())

# except Exception as e:
#     print(e)
#     conn.rollback()
# finally:
#     cur.close()
#     conn.close()
