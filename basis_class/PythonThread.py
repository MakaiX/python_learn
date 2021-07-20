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
        print ("开始线程:" + self.name)
        printTime(self.name, self.counter, 5)

        print("结束线程:" + self.name)


def printTime(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("{0} {1}".format(threadName, time.ctime(time.time())))
        counter -= 1


if __name__ == '__main__':
    thred1 = myThread(1, "Threa-1", 1)
    thred2 = myThread(2, "Threa-2", 2)

    thred1.start()
    thred2.start()
    thred1.join()
    thred2.join()

print("退出线程")
