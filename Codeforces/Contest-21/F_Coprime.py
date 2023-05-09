from collections import defaultdict, Counter, deque
from math import gcd

def runCase():
    n = int(input())
    array = list(map(int, input().split()))
    lastSeen = {val: i + 1 for i, val in enumerate(array)}
    maxRes = -1

    for i in range(1, 1001):
        if i not in lastSeen: continue
        for j in range(i, 1001):
            if j in lastSeen and gcd(i, j) == 1:
                maxRes = max(maxRes, lastSeen[i] + lastSeen[j])
    
    print(maxRes)

if __name__ == '__main__':
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()