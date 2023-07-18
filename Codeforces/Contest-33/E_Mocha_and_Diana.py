from collections import defaultdict, Counter, deque

def runCase():
    n, m1, m2 = map(int, input().split())
    parents1, parents2 = [i for i in range(n + 1)], [i for i in range(n + 1)]
    rank1, rank2 = [1] * (n + 1), [1] * (n + 1)

    def find(e, parent):
        p = parent[e]
        while p != parent[p]:
            parent[p] = parent[parent[p]]
            p = parent[p]
        return p
    def union(e1, e2, parent, rank):
        p1, p2 = find(e1, parent), find(e2, parent)
        if p1 == p2: return False
        if rank[p1] > rank[p2]:
            parent[p2] = p1
            rank[p1] += p2
        else:
            parent[p1] = p2
            rank[p2] += p1
        return True
    
    for _ in range(m1):
        u, v = map(int, input().split())
        union(u, v, parents1, rank1)
    for _ in range(m2):
        u, v = map(int, input().split())
        union(u, v, parents2, rank2)
    
    toadd = []
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if find(i, parents1) != find(j, parents1) and find(i, parents2) != find(j, parents2):
                union(i, j, parents1, rank1)
                union(i, j, parents2, rank2)
                toadd.append((i, j))
    
    print(len(toadd))
    for x in toadd:
        print(*x)

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()