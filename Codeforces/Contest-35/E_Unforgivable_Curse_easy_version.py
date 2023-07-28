from collections import defaultdict, Counter, deque

def runCase():
    n, k = map(int, input().split())
    s = input()
    t = input()
    parent = defaultdict(str)
    rank = defaultdict(lambda: 1)
    for i in range(ord('a'), ord('z') + 1):
        parent[chr(i)] = chr(i)
    
    def find(c):
        p = parent[c]
        while p != parent[p]:
            p = parent[p]
        return p
    
    def union(c1, c2):
        p1, p2 = find(c1), find(c2)
        if p1 == p2: return
        if rank[p1] > rank[p2]:
            parent[p2] = p1
            rank[p1] += rank[p2]
        else:
            parent[p1] = p2
            rank[p2] += rank[p1]
            
    for i in range(n - k):
        union(s[i], s[i + k])
        if i + k + 1 < n:
            union(s[i], s[i + k + 1])
    
    for i in range(n):
        if t[i] not in find(t[i]) != find(s[i]):
            return print('NO')
    
    print('YES')

if __name__ == '__main__':
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()