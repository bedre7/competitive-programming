from collections import defaultdict, Counter, deque

class Node:
    def __init__(self, val, depth=0):
        self.val = val
        self.left = None
        self.right = None
        self.depth = depth
    
    def __repr__(self):
        return f'Node({self.val}, {self.left}, {self.right})'
    
def runCase():
    n = int(input())
    permutation = list(map(int, input().split()))
    deps = defaultdict(int)

    def dfs(start, end, depth=0):
        if start > end: return None
        if start == end: 
            deps[permutation[start]] = depth
            return Node(permutation[start], depth)

        _max = max(permutation[start: end + 1])
        max_index = permutation.index(_max)
        midNode = Node(permutation[max_index], depth)
        deps[permutation[max_index]] = depth
        midNode.left = dfs(start, max_index - 1, depth + 1)
        midNode.right = dfs(max_index + 1, end, depth + 1)

        return midNode

    root = dfs(0, n - 1)
    depths = []
    for p in permutation:
        depths.append(deps[p])
    
    print(*depths)
if __name__ == '__main__':
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()