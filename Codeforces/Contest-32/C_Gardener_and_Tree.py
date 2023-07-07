from collections import defaultdict, Counter, deque
import heapq

def runCase():
    input()
    n, k = map(int, input().split())
    adj = defaultdict(set)
    degree = defaultdict(int)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        adj[u].add(v)
        adj[v].add(u)
        degree[u] += 1
        degree[v] += 1
    
    queue = deque()
    for node in range(1, n + 1):
        if degree[node] <= 1: queue.append(node)
    
    nodes = set([node for node in range(1, n + 1)])    
    while k > 0:
        nextLev = deque()
        nodes -= set(queue)
        if not queue or not nodes: break
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                for nei in adj[curr]:
                    degree[nei] -= 1
                    adj[nei].discard(curr)
                    if degree[nei] == 1 or degree[nei] == 0:
                        nextLev.append(nei)
            k -= 1
        queue = nextLev

    print(len(nodes))

if __name__ == '__main__':
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()