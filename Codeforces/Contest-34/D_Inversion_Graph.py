from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    currMax = components = 0
    for i, num in enumerate(list(map(int, input().split()))):
        currMax = max(currMax, num)
        if currMax == i + 1:
            components += 1

    print(components)

if __name__ == '__main__':
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()