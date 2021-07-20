import gevent


def coroutine_work(coroutine_name):
    for i in range(5):
        print(coroutine_name, i)
        gevent.sleep(1)


gevent.joinall(
    gevent.spawn(coroutine_work, "worker1"),
    gevent.spawn(coroutine_work, "worker2")
)
