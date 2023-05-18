from collections import defaultdict, Counter, deque
import sys
import threading
from functools import lru_cache

def runCase():
    a, b = map(int, input().split())

    def dfs(curr, path):
        if curr > b: return False
        if curr == b:
            return True
        
        path.append(curr * 2)
        if not dfs(curr * 2, path):
            path.pop()
        else: return True
        path.append(curr * 10 + 1)
        if not dfs(curr * 10 + 1, path):
            path.pop()
        else:
            return True
    
    path = [a]
    dfs(a, path)
    if path and path[-1] == b:
        print('YES')
        print(len(path))
        print(*path)
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