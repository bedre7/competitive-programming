from collections import defaultdict, Counter, deque

def runCase():
    n, m = map(int, input().split())
    cats = list(map(int, input().split()))
    tree = defaultdict(list)
    for _ in range(n - 1):
        x, y = map(int, input().split())
        tree[y].append([x, bool(cats[x - 1])])
        tree[x].append([y, bool(cats[y - 1])])
    
    root = 1
    stack = [(root, bool(cats[0]), 0, -1)]
    canGo = 0
    
    while stack:
        node, hasCat, count, prev = stack.pop()
        if hasCat:
            count += 1
        else:
            count = 0
        if count > m:
            continue
        if len(tree[node]) == 1 and node != root:
            canGo += 1
        for child in tree[node]:
                if child[0] != prev:
                    stack.append((child[0], child[1], count, node))
    
    print(canGo)
if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()

"""
4 2

1 1 1 1

1 2

1 4

3 4
"""