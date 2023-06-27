from collections import defaultdict, Counter, deque
import sys
import threading
from functools import lru_cache
import heapq

def runCase():
    n = int(input())
    emptySeats = [(seat, i) for i, seat in enumerate(list(map(int, input().split())), 1)]
    persons = input()
    occupied = []#max
    heapq.heapify(emptySeats)

    ans = []
    for p in persons:
        if p == '0':
            w, index = heapq.heappop(emptySeats)
            ans.append(index)
            heapq.heappush(occupied, (-w, index))
        else:
            w, index = heapq.heappop(occupied)
            ans.append(index)
    
    print(*ans)


def main():
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()