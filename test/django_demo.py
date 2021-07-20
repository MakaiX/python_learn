from wsgiref.simple_server import WSGIServer, WSGIRequestHandler


def make_server(host, port, app, server_class=WSGIServer, handler_class=WSGIRequestHandler):
    """Create a new WSGI server listening on `host` and `port` for `app`"""
    server = server_class((host, port), handler_class)
    server.set_app(app)
    return server


# demo_app可调用对象，接受请求输出结果
def demo_app(environ, start_response):
    from io import StringIO
    stdout = StringIO()
    print("Hello world!", file=stdout)
    print(file=stdout)
    h = sorted(environ.items())
    for k, v in h:
        print(k, '=', repr(v), file=stdout)
    start_response("200 OK", [('Content-Type', 'text/plain; charset=utf-8')])
    return [stdout.getvalue().encode("utf-8")]


if __name__ == '__main__':
    # 通过make_server方法创建WSGIServer实例
    # 传入建议application，demo_app
    httpd = make_server('', 8000, demo_app)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    import webbrowser

    webbrowser.open('http://localhost:8000/xyz?abc')
    # 调用WSGIServer的handle_request方法处理http请求
    httpd.handle_request()  # serve one request, then exit
    httpd.server_close()
