from collections import defaultdict, Counter, deque

def runCase():
    n, k = map(int, input().split())
    maxJoy = float('-inf')

    for _ in range(n):
        f, t = map(int, input().split())
        if t > k:
            maxJoy = max(maxJoy, f - (t - k))
        else:
            maxJoy = max(maxJoy, f)

    print(maxJoy)

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()