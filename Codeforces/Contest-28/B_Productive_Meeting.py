from collections import defaultdict, Counter, deque
import sys
import threading
from functools import lru_cache
import heapq

def runCase():
    n = int(input())
    maxHeap = list([(-int(x), i + 1) for i, x in enumerate(input().split()) if x != '0'])
    heapq.heapify(maxHeap)
    talks = []
    while maxHeap:
        left1, p1 = heapq.heappop(maxHeap)
        if maxHeap:
            left2, p2 = heapq.heappop(maxHeap)
            talks.append((p1, p2))
            if -left1 > 1:
                heapq.heappush(maxHeap, (left1 + 1, p1))
            if -left2 > 1:
                heapq.heappush(maxHeap, (left2 + 1, p2))
        else:
            break

    print(len(talks))
    for talk in talks:
        print(*sorted(talk))


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