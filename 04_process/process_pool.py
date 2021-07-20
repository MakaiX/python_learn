import time, random, os
from multiprocessing import Pool


def worker(msg):
    t_start = time.time()

    print("%s 线程正在运行。。。 %s" % (msg, os.getpid()))

    time.sleep(random.random() * 2)

    t_stop = time.time()
    print("%s 线程执行结束，耗时：%2f s" % (msg, t_stop - t_start))


if __name__ == '__main__':
    # 创建进程池
    po = Pool(3)
    # 使用进程池，调用方法
    for i in range(10):
        po.apply_async(worker, (i,))
    time.sleep(2)
    # 关闭进程池
    po.close()
    # 等待进程完成
    po.join()
