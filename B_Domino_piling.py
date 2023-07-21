from collections import defaultdict, Counter, deque

def runCase():
    a, b = map(int, input().split())
    print(a * b // 2)
if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()