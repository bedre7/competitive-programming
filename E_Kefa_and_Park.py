from collections import defaultdict, Counter, deque

def runCase():
    n, m = map(int, input().split())
    cats = list(map(int, input().split()))
    tree = defaultdict(list)
    childs = set()
    for _ in range(n - 1):
        x, y = map(int, input().split())
        if y in childs:
            tree[y].append([x, True if cats[x - 1] == 1 else False])
            childs.add(x)
        else:
            tree[x].append([y, True if cats[y - 1] == 1 else False])
            childs.add(y)
    
    root = 1
    stack = [(root, bool(cats[0]), 0)]
    canGo = 0
    
    while stack:
        node, hasCat, count = stack.pop()
        if hasCat:
            count += 1
        else:
            count = 0
        if count > m:
            continue
        if len(tree[node]) == 0:
            canGo += 1
        for child in tree[node]:
                stack.append((child[0], child[1], count))
    
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