import sys, threading
from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    parents = list(map(int, input().split()))
    tree = defaultdict(list)

    for i in range(n):
        if parents[i] != i + 1:
            tree[parents[i]].append(i + 1)
    
    paths = []
    children = set([c for childs in tree.values() for c in childs])
    root = [p for p in parents if p not in children][0]
    stack = [root]
    currPath = []
    while stack:
        node = stack.pop()
        currPath.append(node)
        if not tree[node]:
            paths.append(currPath)
            currPath = []
        for child in tree[node]:
            stack.append(child)
    
    print(len(paths))
    for path in paths:
        print(len(path))
        print(*path)

if __name__ == '__main__':
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()