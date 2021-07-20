import socket
import re


def handle_client(new_socket):
    # 接收客户端数据
    recv_data = new_socket.recv(1024).decode("utf-8")
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
        new_socket.send(response_headers.encode("utf-8"))
        new_socket.send(response_body)
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


# 这里配置服务器
DOCUMENTS_ROOT = "./html"

if __name__ == '__main__':
    main()
