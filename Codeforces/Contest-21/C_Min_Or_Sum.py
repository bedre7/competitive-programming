from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    array = list(map(int, input().split()))

    OR = 0
    for a in array:
        OR |= a
    
    print(OR)

if __name__ == '__main__':
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()