import sys, threading
from collections import defaultdict, Counter, deque

def runCase():
    n, D = map(int, input().split())
    players = list(map(int, input().split()))
    players.sort()
    queue = deque(players)
    ans = 0
    
    while queue:
        x = queue.pop()
        power = x
        while queue and power <= D:
            power += x
            queue.popleft()

        if power > D:
            ans += 1

    print(ans)

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()