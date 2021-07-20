import socket


def main():
    # 创建socket
    client_socket = socket.socket()

    # 链接服务器socket
    server_addr = ('', 7788)
    client_socket.connect(server_addr)
    # 发送下载文件的请求
    filename = input('请输入下载文件的名称：')
    client_socket.send(filename.encode('utf-8'))
    # 读取服务器发送的内容
    recv_data = client_socket.recv(1024)
    # 将读取内容写入到新的文件
    if recv_data:
        with open("[接收]" + filename, 'wb') as f:
            f.write(recv_data)
    # 关闭socket
    client_socket.close()


if __name__ == '__main__':
    main()
