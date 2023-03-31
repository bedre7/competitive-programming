import sys, threading
from collections import defaultdict, Counter

def runCase():
    a,b,c,x,y = map(int, input().split())
    x -= a
    y -= b
    r = 0
    r += max(0, x)
    r += max(0, y)
    if r - c <= 0:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()