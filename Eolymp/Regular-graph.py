from collections import defaultdict, Counter, deque

def runCase():
    n, m = map(int, input().split())
    graph = defaultdict(int)

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u] += 1
        graph[v] += 1
    
    print('YES' if len(set(graph.values())) == 1 else 'NO')

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()