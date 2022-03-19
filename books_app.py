import psycopg2
import sys

conn = psycopg2.connect("dbname=books_app user=postgres password=pass host=127.0.0.1")
cur = conn.cursor()

print(sys.argv)

# register
# login
# add
# favorites
# books

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'signup':
        email = ''
        while email == '':
            email = input("Please type your email: \n")

        password = ''
        while password == '':
            password = input("Please type your password: \n")

        firstname = ''
        while firstname == '':
            firstname = input("Please type your firstname: \n")

        lastname = ''
        while lastname == '':
            lastname = input("Please type your lastname: \n")

        try:
            cur.execute("insert into users (firstname, lastname, email, password) values (%s, %s, %s, %s)", (firstname,
                                                                                                             lastname,
                                                                                                             email,
                                                                                                             password))
            conn.commit()
        except Exception as e:
            print(e)
            print('Something went wrong!!!')
