from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    kangaroos = [int(input()) for _ in range(n)]
    kangaroos.sort()
    mid = n // 2
    left = 0
    right = mid

    visible = 0
    while right < n:
        if kangaroos[left] * 2 <= kangaroos[right]:
            visible += 1
        else:
            visible += 2
        left += 1
        right += 1
    
    while left < mid:
        visible += 1
        left += 1
    
    print(visible)

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()