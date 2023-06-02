from collections import defaultdict, Counter, deque
from functools import lru_cache

def runCase():
    n = int(input())
    array = list(map(int, input().split()))
    rules = list(map(int, input()))
    print(rules)

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()