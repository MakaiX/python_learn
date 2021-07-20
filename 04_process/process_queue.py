from multiprocessing import Process, Queue


def put_msg(queue):
    """向队列中存放消息"""
    try:
        if not queue.full():
            for i in range(6):
                queue.put_nowait(i)
                print("put {} 进入队列".format(i))
    except:
        print("队列已满！！！")


def get_msg(queue):
    """从队列中取消息"""
    while True:
        if not queue.empty():
            get_msg = queue.get(True)
            print("接收到的消息是:%s" % get_msg)
        else:
            break


if __name__ == '__main__':
    # 创建队列
    queue = Queue(5)
    # 创建进程
    p1 = Process(target=put_msg, args=(queue,))
    p2 = Process(target=get_msg, args=(queue,))
    p1.start()
    p1.join()
    p2.start()
