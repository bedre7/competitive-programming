import sys, threading
from collections import defaultdict, Counter

def runCase():
    n, m = map(int, input().split())
    dividers = list(map(int, input().split()))
    dividers.sort(reverse=True)

    slots = 2
    if slots >= n:
        print(0)
        return
    
    for i in range(len(dividers)):
        slots += dividers[i] - 1
        if slots >= n:
            print(i + 1)
            break
    else:
        if slots >= n:
            print(i + 1)
        else:
            print(-1)

if __name__ == '__main__':
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()