import sys, threading
from collections import defaultdict, Counter

def runCase():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()

    def bsearch(x):
        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r) // 2
            if a[mid] <= x:
                l = mid + 1
            else:
                r = mid - 1
        
        return l
    
    for i in range(m):
        print(bsearch(b[i]), end=' ')

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()