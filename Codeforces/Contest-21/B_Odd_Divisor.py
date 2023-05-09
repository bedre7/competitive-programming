from collections import defaultdict, Counter, deque
from math import ceil

def runCase():
    n = int(input())
    while n % 2 == 0:
        n /= 2
    
    print('NO' if n == 1 else 'YES')

if __name__ == '__main__':
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()