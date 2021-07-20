import threading
import time

"""验证线程全局共享变量"""
g_num = 0
lock = threading.Lock()


class Work1(threading.Thread):
    def run(self) -> None:
        global g_num
        with lock:
            for i in range(1000000):
                g_num += 1

        print("Work1的值是 %d" % g_num)


class Work2(threading.Thread):
    def run(self) -> None:
        global g_num
        with lock:
            for i in range(1000000):
                g_num += 1

        print("Work2的值是 %d" % g_num)


def main():
    w1 = Work1()
    w2 = Work2()
    w1.start()
    w2.start()
    time.sleep(1)
    print("主程序的值是： %d" % g_num)


if __name__ == '__main__':
    main()
