import sys, threading
from collections import defaultdict, Counter

def runCase():
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

input = lambda: sys.stdin.readline().strip()

def main():
    tests = int(input())

    for _ in range(tests):
        runCase()

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
    print(sys.getrecursionlimit())