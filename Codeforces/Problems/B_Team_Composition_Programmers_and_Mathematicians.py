import sys, threading
from collections import defaultdict, Counter

def runCase():
    n, m = map(int, input().split())
    
    start = 0
    end = min(n, m)
    teams = 0

    while start <= end:
        mid = (start + end) // 2
        if  mid * 4 <= n + m:
            teams = mid
            start = mid + 1
        else:
            end = mid - 1
    
    print(teams)

if __name__ == '__main__':
    testCases = int(input())
    for _ in range(testCases):
        runCase()