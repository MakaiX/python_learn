import threading
from time import sleep


class MyThread(threading.Thread):
    def run(self) -> None:
        for i in range(10):
            sleep(0.5)
            msg = "I'm " + self.name + "@" + str(i)
            print(msg)


def main():

    for i in range(5):
        t = MyThread()
        t.start()


if __name__ == '__main__':
    main()
