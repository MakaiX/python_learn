import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程:" + self.name)
        # 开启锁
        threading_lock.acquire()

        printTime(self.name, self.counter, 5)

        # 关闭锁
        threading_lock.release()
        print("结束线程:" + self.name)


def printTime(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("{0} {1}".format(threadName, time.ctime(time.time())))
        counter -= 1


# 创建锁
threading_lock = threading.Lock()

threads = []

thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for i in threads:
    i.join()

print("退出线程")
