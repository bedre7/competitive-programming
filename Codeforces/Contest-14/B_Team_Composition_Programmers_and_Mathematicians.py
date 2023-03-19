import sys, threading
from collections import defaultdict, Counter

def runCase():
    a, b = map(int, input().split())

    def makeTeam(teams):
        if a == b: return a // 2
        return min(min(a, b), max(a, b) // 3)
    
    print(makeTeam(1))

def main():
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()