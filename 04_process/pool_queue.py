import os
import time
from multiprocessing import Manager, Pool


def reader(q):
    """读消息"""
    print("子进程号：%s，其父进程号是：%s" % (os.getpid(), os.getppid()))

    for i in range(q.qsize()):
        if not q.empty():
            print("reader从队列中获取消息 %s" % (q.get(True)))
        else:
            break


def writer(q):
    """写消息"""
    # 获取子进程&父进程
    print("子进程号：%s，其父进程号是：%s" % (os.getpid(), os.getppid()))
    for i in "HK-life":
        if not q.full():
            q.put(i)
            print("%s 已写入r子进程 %s" % (i, os.getpid()))

    print("-----")


if __name__ == '__main__':
    print("(%s) Start" % os.getpid())

    # 使用manager重的queue创建队列
    q = Manager().Queue()

    # 创建进程池
    p = Pool()

    # 调用进程池，写入数据到队列
    p.apply_async(writer, (q,))

    # 休眠一段时间
    time.sleep(1)
    # 调用进程池，读取数据
    p.apply_async(reader, (q,))
    # 关闭
    p.close()
    p.join()
    print("(%s) End" % os.getpid())
