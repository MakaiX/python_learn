import socket
import time


def main():
    # 创建socket连接
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    local_addr = ('', 7788)
    udp_socket.bind(local_addr)
    # socket发送数据
    # udp_socket.sendto("haha".encode("utf-8"), ('127.0.0.1', 7788))

    while True:
        # 接收数据
        recvfrom = udp_socket.recvfrom(1024)

        print("{},{}".format(recvfrom, time.asctime(time.localtime())))
        print("{}".format(recvfrom[0].decode('utf-8')))
        print("{}".format(recvfrom[1]))
    # 关闭socket
    socket.close(0)

    print("-------")


if __name__ == '__main__':
    main()
