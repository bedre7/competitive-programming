from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    s = input()
    stack = []
    last = 0
    parent = [i for i in range(2 * n)]
    rank = [1 for _ in range(2 * n)]
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

    for i, c in enumerate(s):
        if c == ')':
            j, b = stack.pop()
            union(i, j)
        else:
            if not stack:
                union(i, last)
                last = i
            stack.append((i, c))
    print(parent)
    print(len(set(parent)))

if __name__ == '__main__':
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()