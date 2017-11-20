from wsgiref.simple_server import make_server

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [('<h1>Hello, 这个是一个最简单的web demo!</h1>').encode('utf-8')]


httpd = make_server('', 8000, application)
print('浏览器打开 http://localhost:8000')
httpd.serve_forever()
# C G Am Em F C F G