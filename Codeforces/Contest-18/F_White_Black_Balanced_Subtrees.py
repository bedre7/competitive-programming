from collections import defaultdict, Counter, deque

class Node:
    def __init__(self, val, color):
        self.val = val
        self.color = color
        self.balance = 0
    
    def __repr__(self):
        return f'Node({self.val}, {self.color})'
        
def runCase():
    n = int(input())
    parents = list(map(int, input().split()))
    color = input()
    tree = defaultdict(list)
    for i in range(n - 1):
        tree[parents[i]].append(Node(i + 2, color[i + 1]))
    
    balanced = 0
    def dfs(node):
        nonlocal balanced
        if isinstance(node, Node):
            if not tree[node.val]:
                node.balance = 1 if node.color == 'B' else -1
                return node.balance
            else:
                node.balance += (1 if node.color == 'B' else -1)
        
        black = 0
        white = 0
        parent = node
        if isinstance(node, Node):
            parent = node.val

        for child in tree[parent]:
            if child.color == 'B':
                black += dfs(child)
            else:
                white += dfs(child)
        if isinstance(node, Node):
            node.balance = black + white + (1 if node.color == 'B' else -1)
            print(node, node.balance, black, white)
            balanced += 1 if node.balance == 0 and tree[parent] else 0
        else:
            balanced += 1 if tree[parent] and black + white == 0 else 0
        
        return black + white
    
    dfs(1)
    print(balanced)

if __name__ == '__main__':
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()

"""
[1  ,1  ,2  ,3  ,3  ,5]
a2  a3  a4  a5  a6  a7
"""