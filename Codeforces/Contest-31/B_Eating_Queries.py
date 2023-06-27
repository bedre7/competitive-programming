from collections import defaultdict, Counter, deque
import heapq

def runCase():
    n, q = map(int, input().split())
    sugar = list(map(lambda x: -int(x), input().split()))
    queries = []
    for i in range(q):
        queries.append([int(input()), i])
    heapq.heapify(sugar)

    k = 0
    curr = 0
    ans = [0] * q
    for x, i in sorted(queries):
        while sugar and curr < x:
            curr += -heapq.heappop(sugar)
            k += 1
        if curr >= x: ans[i] = k
        else: ans[i] = -1
    
    for a in ans:
        print(a)
                    
if __name__ == '__main__':
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()
