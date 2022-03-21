import psycopg2
import json

with open('config.json') as f:
    CONFIGS = json.load(f)

DB_CONFIGS = f'dbname={CONFIGS["DB_NAME"]} user={CONFIGS["DB_USER"]} password={CONFIGS["DB_PASSWORD"]} host={CONFIGS["DB_HOST"]}'


def execute(sql, params=None):
    conn = psycopg2.connect(DB_CONFIGS)
    cur = conn.cursor()

    if params is None:
        params = ()

    try:
        cur.execute(sql, params)
        conn.commit()
        return True
    except:
        conn.rollback()
        return False
    finally:
        cur.close()
        conn.close()


def execute_and_get(sql, params=None):
    conn = psycopg2.connect(DB_CONFIGS)
    cur = conn.cursor()

    if params is None:
        params = ()

    try:
        cur.execute(sql, params)
        return cur.fetchone()
    except:
        conn.rollback()
    finally:
        cur.close()
        conn.close()


def execute_and_get_all(sql, params=None):
    conn = psycopg2.connect(DB_CONFIGS)
    cur = conn.cursor()

    if params is None:
        params = ()

    try:
        cur.execute(sql, params)
        return cur.fetchall()
    except:
        conn.rollback()
    finally:
        cur.close()
        conn.close()
