import timeit

def test():
    """Stupid test function"""
    L = []
    for i in range(100):
        L.append(i)

if __name__ == '__main__':
    print timeit.timeit("test()", setup="from __main__ import test")
