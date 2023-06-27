from collections import defaultdict, Counter, deque
from math import lcm

def runCase():
    n = int(input())
    array = list(map(int, input().split()))
    chosen = lcm(*array)
    operations = []
    for i, a in enumerate(array, 1):
        if a == chosen: continue
        operations.append([i, chosen - a])
    
    print(len(operations))
    for op in operations:
        print(*op)

if __name__ == '__main__':
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()