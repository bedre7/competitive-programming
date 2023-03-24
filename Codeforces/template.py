import sys, threading
from collections import defaultdict, Counter

def runCase():
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

def main():
    pass

if __name__ == '__main__':
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()
        import sys, threading

input = lambda: sys.stdin.readline().strip()

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()