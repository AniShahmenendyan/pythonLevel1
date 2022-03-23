from wsgiref.simple_server import make_server


def app(environ, start_response):
    response_body = ''

    request_path = environ['PATH_INFO']
    request_query_string = environ['QUERY_STRING']
    request_method = environ['REQUEST_METHOD']

    users = ['Felix', 'Mher', 'Arsen', 'Davit']
    response_status = '200 OK'

    if request_path == '/':
        response_body = 'Home page!!!'
    elif request_path == '/users':
        response_body = str(users)
    else:
        response_body = 'Not found'
        response_status = '404 NOT FOUND'

    response_headers = [
        ('content-type', 'text/plain'),
    ]

    response_body = response_body.encode()

    start_response(response_status, response_headers)

    return [response_body]


srv = make_server(
    'localhost',
    8000,
    app
)

srv.serve_forever()
