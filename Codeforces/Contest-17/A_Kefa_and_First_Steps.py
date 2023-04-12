from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    array = list(map(int, input().split()))
    longest = 1
    left = 0
    for i in range(1, n):
        if array[i] < array[i-1]:
            left = i
        else:
            longest = max(longest, i - left + 1)

    print(longest)

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()