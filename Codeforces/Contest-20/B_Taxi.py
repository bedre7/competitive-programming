from collections import defaultdict, Counter, deque
from math import ceil

def runCase():
    n = int(input())
    groups = list(map(int, input().split()))
    taxis = 0

    counts = Counter(groups)
    for group, count in counts.items():
        if group == 2:
            taxis += ceil(count / 2)
        elif group == 3:
            ones = counts[1]
            paired = min(count, ones)
            taxis += paired
            count -= paired
            taxis += count
            counts[1] -= paired
            taxis += ceil(counts[1] / 4)
            counts[1] = 0
        elif group == 4:
            taxis += count
    
    if counts[1]:
        taxis += ceil(counts[1] / 4)
    
    print(taxis)

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()