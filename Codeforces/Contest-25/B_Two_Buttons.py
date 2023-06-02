from collections import defaultdict, Counter, deque
from functools import lru_cache

def runCase():
    n, m = map(int, input().split())
    queue = deque()
    queue.append([n, 0])
    used = set()
    used.add(n)

    while queue:
        num, clicks = queue.popleft()
        if num == m: return print(clicks)
        if num - 1 > 0 and num - 1 not in used:
            queue.append([num - 1, clicks + 1])
            used.add(num - 1) 
        if num * 2 not in used and num < m:
            queue.append([num * 2, clicks + 1])
            used.add(num * 2) 

if __name__ == '__main__':  
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()