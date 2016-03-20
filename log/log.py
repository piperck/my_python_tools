# coding: utf-8
import traceback
import sys
import logging


gList = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


logging.basicConfig(
    # 配置日志的输出方式以及格式
    level=logging.DEBUG,
    filename='log.txt',
    filemode='w',
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
)

console = logging.StreamHandler()
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


def f():
    gList[5]
    logging.info('calling method g() in f()')            # 记录正常信息
    return g()


def g():
    logging.info('calling method h() in g()')
    return h()


def h():
    logging.info('Delete element in gList in h()')
    del gList[2]
    return i()


def i():
    logging.info('Append element i to gList in i()')
    gList.append('i')
    print gList[7]


if __name__ == '__main__':
    logging.debug('Information during calling f():')
    try:
        f()
    except IndexError as ex:
        print "Sorry,Exception occured,you accessed an element out of range"

        # traceback.print_exc()

        tt, tv, tb = sys.exc_info()

        # 记录异常信息
        logging.error("Sorry,Exception occured, you accessed an element out of range")
        logging.critical('object info: %s' % ex)

        # 记录异常对应值
        logging.critical('Error Type:{0},Error Information:{1}'.format(tt, tv))

        # 记录具体的TRACE信息
        logging.critical(''.join(traceback.format_tb(tb)))

        sys.exit(1)


