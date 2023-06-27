from collections import defaultdict, Counter, deque
import sys
import threading
from functools import lru_cache
import heapq

def runCase():
    n = int(input())
    operations = []
    minHeap = []
    for _ in range(n):
        curr = input()
        if curr.startswith("insert"):
            operations.append(curr)
            num = int(curr.split()[1])
            heapq.heappush(minHeap, num)
        elif curr.startswith("getMin"):
            num = int(curr.split()[1])
            if not minHeap:
                heapq.heappush(minHeap, num)
                operations.append("insert " + str(num))
                operations.append(curr)
            elif num == minHeap[0]: 
                operations.append(curr)
            else:
                while minHeap and minHeap[0] < num:
                    operations.append("removeMin")
                    heapq.heappop(minHeap)
                if not minHeap or (minHeap and minHeap[0] != num):
                    heapq.heappush(minHeap, num)
                    operations.append("insert " + str(num))
                operations.append(curr)
        else:
            if not minHeap:
                heapq.heappush(minHeap, 1)
                operations.append("insert 1")
            operations.append(curr)
            heapq.heappop(minHeap)
    
    print(len(operations))
    for op in operations:
        print(op)

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