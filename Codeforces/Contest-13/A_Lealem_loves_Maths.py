import sys, threading
from collections import defaultdict, Counter

def runCase():
    exp = list(map(str, sorted(list(map(int, input().split('+'))))))
    print('+'.join(exp))

if __name__ == '__main__':
    runCase()