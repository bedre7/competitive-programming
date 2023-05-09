from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())

    if n == 2:
        print(2)
    else:
        print(3)
        
if __name__ == '__main__':
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()