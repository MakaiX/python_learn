import time

from greenlet import greenlet


def work1():
    while True:
        print("---A---")
        gr2.switch()
        time.sleep(0.1)


def work2():
    while True:
        print("---B---")
        gr1.switch()
        time.sleep(0.1)


gr1 = greenlet(work1)
gr2 = greenlet(work2)

gr1.switch()
