import os


def walk_dir(path):
    for root, dirs, files in os.walk(path, topdown=True):
        print root
        print dirs
        print files


if __name__ == '__main__':
    walk_dir('/Users/piperck/Desktop/ninelie EP')

