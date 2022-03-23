from wsgiref.simple_server import make_server


def app(environ, start_response):
    response_body = b'Hello World!!!'
    response_status = '200 OK'

    response_headers = [
        ('Location', 'https://google.com'),
        ('content-type', 'text/plain'),
        ('content-length', str(len(response_body)))
    ]
    response_status = '302 '

    start_response(response_status, response_headers)

    return [response_body]


srv = make_server(
    '0.0.0.0',
    8000,
    app
)

srv.serve_forever()
