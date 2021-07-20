import socket


def main():
    pass
    # 创建套接字
    server_socket = socket.socket()
    # 绑定地址
    serv_addr = ('', 7788)
    server_socket.bind(serv_addr)
    # 监听链接
    server_socket.listen(128)
    # 创建客户端socket，接收消息
    client_socket, client_addr = server_socket.accept()
    client_socket.recv(1024)
    # 发送消息
    client_socket.send('This is a file!'.encode('utf-8'))
    # 关闭套接字
    client_socket.close()
    server_socket.close()


if __name__ == '__main__':
    main()
