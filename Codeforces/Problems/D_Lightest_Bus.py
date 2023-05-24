from collections import defaultdict, Counter, deque
import sys
import threading
from functools import lru_cache

def runCase():
    n = int(input())
    students = list(map(int, input().split()))
    minWeight = float('inf')

    def dfs(start, capacity):
        nonlocal minWeight
        if start == n: return float('inf')
        if start + capacity < n:
            minWeight = min(minWeight, 
                            sum(students[start : start + capacity]),
                            dfs(start + capacity, 12), 
                            dfs(start + capacity, 18)
                            )
        else: 
            minWeight = min(minWeight, sum(students[start: ]))
            return minWeight
        
    dfs(0, 12)
    dfs(0, 18)
    print(minWeight)

def main():
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()