from collections import defaultdict, Counter, deque
import heapq
import math

def runCase():
    n = int(input())
    m = int(input())
    seats = []
    for _ in range(n):
        seats.append(int(input()))
    MAX = max(seats)
    for i in range(n):
        seats[i] = [seats[i], i]

    heapq.heapify(seats)
    needed = m
    while seats and needed > 0:
        curr, i = heapq.heappop(seats)
        if curr == MAX: 
            break
        else:
            needed -= (MAX - curr)
    
    mink, maxk = MAX, MAX + m
    if needed > 0:
        mink = MAX + math.ceil(needed / n)
        
    print(mink, maxk)


if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()
