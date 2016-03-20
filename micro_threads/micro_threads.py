# coding: utf-8
import gevent.monkey
gevent.monkey.patch_socket()
import gevent
import datetime
import requests

proxies = {
  "http": "localhost:8888",
  "https": "localhost:8888",
}

def fetch(pid, now_time):
    URL = 'http://www.xiachufang.com/downloads/baidu_pip/2016030511.json'       # xcf_本周最佳推荐
    # 解释时间参数
    # 这样抓取会得到一个文件
    gevent.sleep(1)
    response = requests.get(URL.replace(URL[46:-5], now_time), proxies=proxies)
    result = response.json()
    result_count = result['count']

    print 'process pid: %s and xcf_info_count: %s' % (pid, result_count)
    return result_count


def asynchronous(now_time):
    micro_threads = []
    # 开多少个micro_threads去抓?
    for i in range(1, 10000):
        micro_threads.append(gevent.spawn(fetch, i, (now_time-datetime.timedelta(hours=i)).strftime('%Y%m%d%H')))
    gevent.joinall(micro_threads)


print 'Asychronous: '
now_time = datetime.datetime.now()
asynchronous(now_time)