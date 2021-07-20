from multiprocessing.context import Process
import os
import time


def run_proc():
    print("子进程运行中，pid={}".format(os.getpid()))
    for i in range(5):
        print("---->" + str(i))

    print("子进程结束运行。。。")


if __name__ == '__main__':
    p1 = Process(target=run_proc)
    p1.start()
    print("父进程运行中，pid={}".format(os.getpid()))
    p1.join()

    print("父进程结束运行。。。")
