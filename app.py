import psycopg2

conn = psycopg2.connect("dbname=python_level1 user=postgres password=pass host=127.0.0.1")
cur = conn.cursor()

cur.execute('select * from users')

print(cur.fetchone())
print(cur.fetchone())
print(cur.fetchone())
print(cur.fetchone())
# print(cur.fetchall())

# cur.execute("insert into users (firstname, lastname, email) values ('Davit', 'Melikyan', 'melikyan@gmail.com')")
# conn.commit()

cur.execute('select * from users')
print(cur.fetchall())