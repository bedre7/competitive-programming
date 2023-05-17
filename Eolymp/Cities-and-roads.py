from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    count = 0
    for _ in range(n):
        count += list(map(int, input().split())).count(1)
    print(count // 2)

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()