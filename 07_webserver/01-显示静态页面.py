import socket


def handle_client(new_socket):
    recv_data = new_socket.recv(1024).decode("utf-8")
    print(recv_data)

    response_headers = "HTTP/1.1 200 OK\r\n"
    response_headers += "\r\n"
    response_body = "hahaha"
    response = response_headers + response_body
    new_socket.send(response.encode("utf-8"))

    # 关闭新的链接
    new_socket.close()


def main():
    # 创建TCP链接服务端
    tcp_socket = socket.socket()
    # 绑定端口
    tcp_socket.bind(('', 7890))
    # 创建监听
    tcp_socket.listen(128)
    while True:
        # accept数据，创建新的客户端
        new_socket, new_addr = tcp_socket.accept()
        # 返回数据
        handle_client(new_socket)
    tcp_socket.close()


if __name__ == '__main__':
    main()
