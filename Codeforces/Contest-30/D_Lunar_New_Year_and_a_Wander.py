from collections import defaultdict, Counter, deque
import heapq

def runCase():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        if u == v or u in graph[v] or v in graph[u]: continue
        graph[u].append(v)
        graph[v].append(u)
    
    heap = graph[1].copy()
    heapq.heapify(heap)
    path = [1]
    visited = [False] * (n + 1)
    visited[1] = True
    for x in heap: visited[x] = True

    while heap:
        curr = heapq.heappop(heap)
        path.append(curr)
        for c in graph[curr]:
            if not visited[c]:
                heapq.heappush(heap, c)
                visited[c] = True
    
    print(*path)

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()