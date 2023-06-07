from collections import defaultdict, Counter, deque
import sys
import threading
from functools import lru_cache

def runCase():
    n, m = map(int, input().split())
    
    odd = ['.' * (m - 1) + '#', '#' + '.' * (m - 1)]
    j = 0
    for i in range(n):
        if i % 2 == 0:
            print('#' * m)
        else:
            print(odd[j])   
            j = 1 - j
    
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