import sys, threading
from collections import defaultdict, Counter

def runCase():
    n, a, b = map(int, input().split())
    x = list(map(int, input().split()))

    j1 = s1 = j2 = s2 = res = 0
    for i in range(n):
    
        while j1 < n and s1 + x[j1] < a:
            s1 += x[j1]
            j1 += 1
            
        while j2 < n and s2 + x[j2] <= b:
            s2 += x[j2]
            j2 += 1
            
        res += j2 - j1 
        s1 -= x[i]
        s2 -= x[i]

    print(res)

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()