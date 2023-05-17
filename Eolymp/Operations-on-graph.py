from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    k = int(input())
    graph = defaultdict(list)
    for _ in range(k):
        operation = list(map(int, input().split()))
        if len(operation) == 3:
            _, u, v = operation
            graph[u].append(v)
            graph[v].append(u)
        else:
            _, v = operation
            print(*graph[v])

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()