from collections import defaultdict, Counter, deque
import sys
import threading
from functools import lru_cache

def runCase():
    n, h = map(int, input().split())
    heights = list(map(int, input().split()))
    width = 0
    for x in heights:
        if x > h:
            width += 2
        else:
            width += 1
    
    print(width)

def main():
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()