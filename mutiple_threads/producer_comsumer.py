# coding:utf-8
import Queue
import time
import random
import threading


# write_lock = threading.Lock()                                                 # 创建primitive锁对象用于控制输出


class Producer(threading.Thread):
    # q传递一个队列参数, con传递了一个链接, name传递了一个名字
    def __init__(self, q, name):
        super(Producer, self).__init__()
        self.q = q
        # self.con = con
        self.name = name
        print "Producer " + self.name + "Started"

    def run(self):
        while True:
            # 锁对象常用的acquire获得锁方法和release释放锁方法
            # 这里使用的是Thread的Condition对象
            # self.con.acquire()
            if self.q.full():
                print 'Queue is full, producer wait!'

                # 手动挂起,并且只能在获得Lock的情况下才可以使用 否则会触发RuntimeError
                # 调用wait()会释放Lock 直到该线程被notify(),notifyall()或超时该线程又重新获得Lock
                # self.con.wait()
            else:
                value = random.randint(0, 10)
                print self.name + " put " + str(value) + "into queue"
                self.q.put((self.name+":"+str(value)))                    # 放置到队列中

                # 通知消费者,notify通知其他线程,被挂起的线程接到通知后会开始运行
                # 默认通知一个正在等待该condition的线程,最多唤醒n个线程 必须在获得Lock的情况下使用否则会报错.
                # self.con.notify()
                # self.con.release()                                            # 释放锁对象


class Consumer(threading.Thread):
    def __init__(self, q, name):
        super(Consumer, self).__init__()
        self.q = q
        # self.con = con
        self.name = name
        print "Consumer " + self.name + "started\n"

    def run(self):
        while True:
            # Condition常用的acquire获得锁方法和release释放锁方法
            # self.con.acquire()
            if self.q.empty():
                print 'queue is empty, consumer wait!'
                # self.con.wait()
            else:
                value = self.q.get()                                            # 从队列中取消息
                print self.name + " get " + value + "from queue"

                # 发送消息通知生产者
                # self.con.notify()
                # self.con.release()                                              # 释放锁对象
                print 'queue still have ' + str(q.qsize()) + 'task\n'


if __name__ == "__main__":
    q = Queue.Queue(10)

    # 使用Condition对象可以在某些事件触发或达到特定的条件后才处理数据.
    # con = threading.Condition()

    # 两个生产者
    p1 = Producer(q, "P1")
    p2 = Producer(q, "P2")
    c1 = Consumer(q, "C1")
    p2.start()
    p1.start()
    c1.start()
