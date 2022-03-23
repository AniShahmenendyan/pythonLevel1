from wsgiref.simple_server import make_server
import psycopg2


def get_users(name_param=None):
    sql = 'select firstname from users'
    params = ()

    if name_param:
        sql += ' where LOWER(firstname) like %s'
        params = ('%' + name_param.lower() + '%',)

    conn = psycopg2.connect("dbname=python_level1 user=postgres password=pass host=127.0.0.1")
    cur = conn.cursor()
    cur.execute(sql, params)
    users = cur.fetchall()
    cur.close()
    conn.close()

    users_names = [user[0] for user in users]
    return users_names


def get_user_by_id(user_id):
    sql = 'select id, firstname, lastname, email from users where id = %s'
    params = (int(user_id),)

    conn = psycopg2.connect("dbname=python_level1 user=postgres password=pass host=127.0.0.1")
    cur = conn.cursor()
    cur.execute(sql, params)
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user


def app(environ, start_response):
    respose_body = '<html><body><meta name="viewport" content="width=device-width, initial-scale=1.0">'

    status = '200 OK'

    request_method = environ.get('REQUEST_METHOD')
    request_path = environ.get('PATH_INFO')
    request_query = environ.get('QUERY_STRING')
    request_user = environ.get('HTTP_USER_AGENT')

    request_query_part_dict = {}
    if request_query != '':
        request_query_parts = request_query.split('&')
        for request_query_part in request_query_parts:
            request_query_part = request_query_part.split('=')
            request_query_part_dict[request_query_part[0]] = request_query_part[1]

    request_path = request_path.strip('/')
    request_path_parts = request_path.split('/')

    if request_path == '' and request_method == 'GET':
        respose_body += 'Welcome to home page!!!'
    elif request_path_parts[0] == 'users' and len(request_path_parts) == 1:

        name_param = request_query_part_dict.get('name', None)
        users_names = get_users(name_param)

        respose_body += ', '.join(users_names)


    elif request_path_parts[0] == 'users' and len(request_path_parts) == 2 and (request_path_parts[1]).isnumeric():
        user_id = int(request_path_parts[1])

        user = get_user_by_id(user_id)

        respose_body += str(user)
    else:
        respose_body += 'Page not found!!!'
        status = '404 NOT FOUND'

    respose_body += '</body>'
    respose_body = respose_body.encode()

    response_headers = [
        ('Content-Type:', 'text/plain',),
        ('Content-Length', str(len(respose_body)))
    ]

    start_response(status, response_headers)

    return [respose_body]


httpd = make_server(
    'localhost',
    8000,
    app
)
while True:
    httpd.handle_request()
