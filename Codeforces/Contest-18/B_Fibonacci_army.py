from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    prev = curr = 1
    
    for _ in range(2, n + 1):
        temp = prev
        prev = curr
        curr = temp + curr
    
    print(curr)

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()