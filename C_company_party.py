from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    company = defaultdict(list)
    roots = []

    for i in range(1, n + 1):
        parent = int(input())
        if parent == -1:
            roots.append(i)
        else:    
            company[parent].append(i)
    
    maxDepth = 0
    for root in roots:
        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            maxDepth = max(maxDepth, depth)
            for child in company[node]:
                queue.append((child, depth + 1))
    
    print(maxDepth)

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()