from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    graph = [[0] * n for _ in range(n)]

    for i in range(n):
        line = list(map(int, input().split()))
        for j in range(1, line[0] + 1):
            graph[i][line[j] - 1] = 1
    
    for row in graph:
        print(*row)


if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()