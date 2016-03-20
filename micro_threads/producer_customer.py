# coding: utf-8
# 生产消费模型
import gevent
from gevent.queue import Queue

tasks = Queue()

def worker(n):
    while not tasks.empty():
        task = tasks.get()
        print 'worker %s got task %s' % (n, task)
        # 切换控制权
        gevent.sleep(0)

    print 'Quitting time! '

def boss():
    for i in xrange(1, 25):
        tasks.put_nowait(i)

gevent.spawn(boss).join()

gevent.joinall([
    gevent.spawn(worker, 'steve'),
    gevent.spawn(worker, 'john'),
    gevent.spawn(worker, 'nancy'),
])
