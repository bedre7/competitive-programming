from collections import defaultdict, Counter, deque
import sys
import threading
from functools import lru_cache

def runCase():
    num = input()
    n = len(num)
    magic = ['1', '14', '144']

    def backtrack(start, end):
        if end - start >= 4: return False
        if num[start: end] in magic:
            if end == n: return True
            if backtrack(end, end + 1):
                return True
        
        if backtrack(start, end + 1):
            return True
        
        return False
        
    if backtrack(0, 1):
        print('YES')
    else:
        print('NO')

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