import socket
import multiprocessing
import re

SERVER_ADDR = IP, PORT = '', 7890
DOCUMENTS_ROOT = "./html"


class WSGIServer(object):
    def __init__(self, server_address):
        # 创建socket链接
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 绑定地址
        self.socket_server.bind(server_address)
        # 允许立即使用上一次绑定的port
        self.socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 创建监听，改为被动
        self.socket_server.listen(1024)
        # 声明root目录
        self.DOCUMENTS_ROOT = DOCUMENTS_ROOT

        # print(self.socket_server)

    def serve_forever(self):
        while True:
            client_socket, client_addr = self.socket_server.accept()
            # print(client_addr)  # test
            # 创建新的进程
            p = multiprocessing.Process(target=self.handleRequest, args=(client_socket,))
            # 启动进程
            p.start()
            # 父进程新的链接
            client_socket.close()

    def handleRequest(self, client_socket):
        # 接收客户端数据
        recv_data = client_socket.recv(1024).decode("utf-8")
        data_split = recv_data.splitlines()
        # for line in data_split:
        #     print(line)
        # print(data_split)
        # print(data_split[0])

        # 获取客户端请求的页面路径
        get_file_name = re.search(r'[^/]+(/[^ ]*)', data_split[0]).group(1)
        # print(get_file_name)

        # 判断获取的文件名称
        if get_file_name == "/":
            get_file_name = DOCUMENTS_ROOT + "/index.html"
        else:
            get_file_name = DOCUMENTS_ROOT + get_file_name

        # 打开文件，并对可能出现的问题就行纠正
        try:
            f = open(get_file_name, 'rb')
        except IOError:
            response_headers = "HTTP/1.1 404 not found\r\n"
            response_headers += "\r\n"
            response_body = "不知道出现了什么问题".encode("utf-8")
        else:
            # 给客户端发送数据
            response_headers = "HTTP/1.1 200 OK\r\n"
            response_headers += "\r\n"
            response_body = f.read()  # 此处读取文件内容为bytes类型
            f.close()
        finally:
            # header 和 body 编码方式不同，分开发送
            # response = response_headers + response_body
            client_socket.send(response_headers.encode("utf-8"))
            client_socket.send(response_body)
            # 子进程关闭链接
            client_socket.close()


def main():
    httpd = WSGIServer(SERVER_ADDR)
    print("web Server: Serving HTTP on port %d ...\n" % PORT)
    httpd.serve_forever()


if __name__ == '__main__':
    main()
