from collections import defaultdict, Counter, deque
import heapq

def runCase():
    string = list(input())
    heap = []
    for i, c in enumerate(string):
        heap.append((-ord(c), i))
    heapq.heapify(heap)

    ans = []
    while heap:
        ascii, i = heapq.heappop(heap)
        if not ans or ans[-1][1] < i:
            ans.append((chr(-ascii), i))
    
    print(''.join([c for c, i in ans]))

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()