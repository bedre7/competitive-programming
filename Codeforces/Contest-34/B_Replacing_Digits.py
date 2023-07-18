from collections import defaultdict, Counter, deque
import heapq

def runCase():
    a = [int(c) for c in input()]
    b = [-int(c) for c in input()]
    heapq.heapify(b)

    for i in range(len(a)):
        if b and -b[0] > a[i]:
            a[i] = -heapq.heappop(b)
    
    print(''.join([str(num) for num in a]))

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()