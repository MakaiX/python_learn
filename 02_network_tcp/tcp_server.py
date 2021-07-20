"""定义tcp链接服务端"""
from socket import *


def main():
    # 创建socket
    tcp_server = socket(AF_INET, SOCK_STREAM)
    # 绑定地址
    dest_addr = ('', 7890)
    tcp_server.bind(dest_addr)
    # 使用listen，将主动socket变为被动
    tcp_server.listen(128)

    while True:
        # accept 客户端的链接
        client_socket, client_addr = tcp_server.accept()
        print('客户端的地址：{}'.format(client_addr))

        # 接收消息
        recv_data = client_socket.recv(1024)
        print("接收到的消息是：{}".format(recv_data.decode('utf-8')))
        # 发送消息
        client_socket.send('已收到消息！！！'.encode('utf-8'))
        client_socket.close()
    # 关闭链接
    tcp_server.close()


if __name__ == '__main__':
    main()
