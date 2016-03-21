import os, sys

def lister(root):
    for (dirname, subshere, fileshere) in os.walk(root):
        for file in fileshere:
            print os.path.join(dirname, file)

if __name__ == '__main__':
    lister(sys.argv[1])


