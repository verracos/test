from flaskapp import app as application

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('0.0.0.0', 8080, application)
    httpd.serve_forever()