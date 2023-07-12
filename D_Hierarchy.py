from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    input()
    paired = set([i for i in range(1, n + 1)])
    costs = defaultdict(lambda: float("inf"))
    m = int(input())
    for _ in range(m):
        a, b, c = map(int, input().split())
        costs[b] = min(costs[b], c)
        paired.discard(b)
    
    if len(paired) == 1:
        print(sum(costs.values()))
    else:
        print(-1)


if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()