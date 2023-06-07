from collections import defaultdict, Counter, deque
import sys
import threading
from functools import lru_cache

def runCase():
    n = int(input())
    array = list(map(int, input().split()))
    possible = [bool(int(c)) for c in input()]

    currMax = 0
    for i in range(n - 1):
        currMax = max(currMax, array[i])
        if currMax > i + 1 and not possible[i]:
            return print('NO')
    
    print('YES')

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