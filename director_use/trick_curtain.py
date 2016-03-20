#!/usr/bin/env python
# Author: piperck <w19890729wai@hotmail.com>.

__version__ = '1.0'
__all__ = [
    'argparse',
    'simplejson',
    'requests',
]


import argparse
import simplejson
import requests


# add a funny start
class CurtainAdapter(object):
    def __init__(self):
        args = self.init()
        self.area = args.a
        self.number = args.n
        self.option = args.o
        self.times = args.t
        # self.test = args.tt

    def init(self):
        # first param is a key word and second param just a alias
        parser = argparse.ArgumentParser(description='to rule the xcf_curtain')
        parser.add_argument('a', choices=['A', 'B'], help='xcf_curtain area')
        parser.add_argument('n', help='xcf_curtain number{1-16}')
        parser.add_argument('o', choices=['close', 'open', 'stop'], help='xcf_curtain option involve close/stop/open')
        parser.add_argument('-t', type=int, help='xcf_curtain move times', default=1)
        # parser.add_argument('-tt', '--test', help='test_interface')

        # deal with input argv
        args = parser.parse_args()

        return args

    def send(self):
        n = 0
        while n < self.times:
            if self.option == 'close' or 'open':
                params = {
                    "ab": self.area,
                    "number": self.number,
                    "op": self.option,
                }
                requests.post('http://cl.xcf.io/clrc', data=params, timeout=1)
                params['op'] = 'stop'
                requests.post('http://cl.xcf.io/clrc', data=params, timeout=1)
        return 'we have moved!!!'

if __name__ == '__main__':
    argv_input = CurtainAdapter()
    argv_input.send()


