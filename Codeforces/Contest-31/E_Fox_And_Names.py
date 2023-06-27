from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    curr = input()
    order = ""
    graph = defaultdict(list)
    indegree = defaultdict(int)
    for _ in range(1, n):
        _next = input()
        i = 0
        m = min(len(curr), len(_next))
        while i < m and curr[i] == _next[i]: i += 1

        if i < m:
            graph[curr[i]].append(_next[i])
            indegree[_next[i]] += 1
        elif len(curr) > len(_next):
            return print("Impossible")
        curr = _next

    queue = deque()
    for i in range(ord('a'), ord('z') + 1):
        if indegree[chr(i)] == 0: queue.append(chr(i))
    
    while queue:
        curr = queue.popleft()
        order += curr
        for nei in graph[curr]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                queue.append(nei)
    
    if len(order) != 26: print("Impossible")
    else: print(order)

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()
