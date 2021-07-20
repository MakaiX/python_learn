import threading
from time import sleep, ctime


def sing(nums):
    for i in range(nums):
        print("正在唱歌：{}".format(i))
        sleep(1)


def dance(nums):
    for i in range(nums):
        print("正在跳舞：{}".format(i))
        sleep(1)


def main():
    t1 = threading.Thread(target=sing, args=(5,))
    t2 = threading.Thread(target=dance, args=(5,))
    t1.start()
    t2.start()

    while True:
        thread = threading.enumerate()
        print("-----线程个数-----：{}".format(len(thread)))

        if len(thread) <= 1:
            break
        sleep(1)


if __name__ == '__main__':
    main()
