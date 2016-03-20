import grequests
import requests
import timeit

proxies = {
  "http": "localhost:8888",
  "https": "localhost:8888",
}

urls = [
    'http://www.xiachufang.com/downloads/baidu_pip/2016030101.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030102.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030103.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030104.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030105.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030106.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030107.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030108.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030109.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030110.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030111.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030112.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030113.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030114.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030115.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030116.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030117.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030118.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030119.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030120.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030121.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030122.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030123.json',
    'http://www.xiachufang.com/downloads/baidu_pip/2016030200.json',
]
def haha():
    rs = (grequests.get(u, proxies=proxies) for u in urls)
    grequests.map(rs)
#
# cProfile.run("haha(urls)")

def hehe():
    hehe = [requests.get(i, proxies=proxies) for i in urls]

#
# cProfile.run("hehe(urls)")


def test():
    """Stupid test function"""
    L = []
    for i in range(100):
        L.append(i)

if __name__ == '__main__':
    print timeit.timeit("hehe()", setup="from __main__ import hehe", number=1)
