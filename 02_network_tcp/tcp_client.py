import socket


def main():
    pass
    # 定义tcp链接
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定地址
    dest_addr = ''
    dest_port = 7890
    tcp_client.connect((dest_addr, dest_port))
    # 发送消息
    send_data = input("请输入发送内容：")
    tcp_client.send(send_data.encode('utf-8'), 1024)
    # 接收消息
    recv_data = tcp_client.recv(1024)
    print("接收到的数据是:{}".format(recv_data.decode('utf-8')))
    # 关闭socket
    tcp_client.close()


if __name__ == '__main__':
    main()
