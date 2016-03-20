#!/usr/bin/env python
# coding:utf-8
import argparse


class ParseCn(object):
    def __init__(self):
        args = self.init()
        self.msg = args.m
        self.uc = args.u

    def init(self):
        # first param is a key word and second param just a alias
        parser = argparse.ArgumentParser(description='parse code')
        parser.add_argument('-m', type=str, help='string codes')
        parser.add_argument('-u', type=str, help='unicode parse')

        # deal with input argv
        args = parser.parse_args()

        return args

    def parse_utf_8(self):
        return self.msg.decode('unicode_escape')

    def parse_unicode(self):
        return u'{0}'.format(self.uc)

if __name__ == '__main__':
    x = ParseCn()
    if x.uc:
        print x.parse_unicode()
    else:
        print x.parse_utf_8()




