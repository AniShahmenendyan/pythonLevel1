import hashlib
import json
from db import execute, execute_and_get, execute_and_get_all

with open('config.json') as f:
    CONFIGS = json.load(f)


def add_user(firstname, lastname, email, password):
    # password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    dk = hashlib.pbkdf2_hmac('sha256', bytes(password, 'utf-8'), bytes(CONFIGS['SALT'], 'utf-8'), 100000)
    password = dk.hex()

    sql = """
    INSERT INTO users (firstname, lastname, email, password) VALUES (%s, %s, %s, %s)
    """
    return execute(sql, (firstname, lastname, email, password))


def get_user(email, password):
    # password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    dk = hashlib.pbkdf2_hmac('sha256', bytes(password, 'utf-8'), bytes(CONFIGS['SALT'], 'utf-8'), 100000)
    password = dk.hex()

    sql = """
    SELECT id, email FROM users  WHERE users.email = %s AND users.password=%s
    """

    return execute_and_get(sql, (email, password))


def get_books():
    sql = """
    SELECT books.id, books.name, books.author 
    FROM books
    """

    return execute_and_get_all(sql)


def add_to_favorites(book_id, user_id):
    sql = """
    INSERT INTO favorites (book_id, user_id) VALUES (%s, %s)
    """

    return execute(sql, (book_id, user_id))


def remove_favorites(book_id, user_id):
    sql = """
    DELETE FROM favorites WHERE book_id = %s AND user_id = %s
    """

    return execute(sql, (book_id, user_id))


def get_favorites(user_id):
    sql = """
    SELECT books.id, books.name, books.author
    FROM favorites 
    LEFT JOIN books on books.id = favorites.book_id 
    WHERE favorites.user_id = %s
    """

    return execute_and_get_all(sql, (user_id,))
