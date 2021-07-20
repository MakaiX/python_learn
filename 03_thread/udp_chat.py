import socket
import threading


def send_msg(udp_socket, dest_ip, dest_port):
    while True:
        send_data = input("请输入：")

        print(send_data)
        udp_socket.sendto(send_data.encode('utf-8'), (dest_ip, dest_port))


def recv_msg(udp_socket):
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print("已收到来自{} 消息：{}".format(str(recv_data[1]), recv_data[0].decode("utf-8")))


def main():
    """创建多线程upd聊天器客户端"""
    # 创建socket链接
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定地址
    dest_addr = ('', 7890)
    udp_socket.bind(dest_addr)

    dest_ip = input("请输入IP：")
    dest_port = int(input("请输入Port："))

    t1 = threading.Thread(target=recv_msg, args=(udp_socket,))

    t1.start()

    send_msg(udp_socket, dest_ip, dest_port)
    # 关闭socket
    # udp_socket.close()


if __name__ == '__main__':
    main()
