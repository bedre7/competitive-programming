import sys, threading
from collections import defaultdict, Counter

def runCase():
    w, et, ef = map(int, input().split())
    time = 0

    if w * ef < ef * et + et * ef:
        time += w * ef
        time += min(w, et) * (4 - ef)
    else:
        time += min(ef * et + et * 4, w * 4)
    
    print(time)

if __name__ == '__main__':
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()