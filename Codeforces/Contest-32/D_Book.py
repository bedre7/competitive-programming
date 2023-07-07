from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    adj = defaultdict(list)
    indegree = defaultdict(int)
    for chapter in range(1, n + 1):
        toread = list(map(int, input().split()))
        if len(toread) == 0: continue
        for i in range(1, len(toread)):
            prev = toread[i]
            adj[prev].append(chapter)
            indegree[chapter] += 1
    
    queue = deque()
    for chapter in range(1, n + 1):
        if indegree[chapter] == 0: queue.append((chapter, 1))
    
    if not queue: return print(-1)
    read = set()
    totalReads = 1
    while queue:
        chapter, reads = queue.popleft()
        totalReads = max(totalReads, reads)
        read.add(chapter)
        for other in adj[chapter]:
            indegree[other] -= 1
            if other < chapter: totalReads = max(totalReads, reads + 1)
            if indegree[other] == 0:   
                if other < chapter:
                    queue.append((other, reads + 1))
                else: queue.append((other, reads))
    
    if len(read) != n: print(-1)
    else: print(totalReads)

if __name__ == '__main__':
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()