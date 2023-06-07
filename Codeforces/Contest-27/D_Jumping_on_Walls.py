from collections import defaultdict, Counter, deque

def runCase():
    n, k = map(int, input().split())
    visited = set()
    wall = []
    for _ in range(2):
        wall.append(input())
    queue = deque([(0, 0)])
    visited.add((0, 0))
    lev = 0
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if (lev < y and y >= n) or (lev < y + k and y + k >= n): return print("YES")
            if lev < y + k and wall[1 - x][y + k] == '-' and (1 - x, y + k) not in visited:
                queue.append((1 - x, y + k))
                visited.add((1 - x, y + k))
            if lev < y + 1 and wall[x][y + 1] == '-' and (x, y + 1) not in visited:
                queue.append((x, y + 1))
                visited.add((x, y + 1))
            if lev < y - 1 and y - 1 >= 0 and wall[x][y - 1] == '-' and (x, y - 1) not in visited:
                queue.append(((x, y - 1)))
                visited.add((x, y - 1))
        lev += 1

    print("NO")

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()
