from collections import deque, defaultdict
def closestStraightCity(c, x, y, q):
    def findDistance(x1, y1, x2, y2):
        return abs(x2 - x1) + abs(y2 - y1)
    
    coords = defaultdict(list)
    for i in range(len(c)):
        coords[c[i]].append(x[i])
        coords[c[i]].append(y[i])
        
    cities = defaultdict(str)
    for i in range(len(c)):
        cities[(x[i], y[i])] = c[i]

    ROW_START, ROW_END = min(y), max(y)
    COL_START, COL_END = min(x), max(x)
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    closest = []
    queue = deque()
    visited = set()
    for i in range(len(q)):    
        if not q[i] in c: continue
        X, Y = coords[q[i]]
        queue.clear()
        queue.append((q[i], X, Y, 0))
        visited.clear()
        visited.add((X, Y))
        nearest = 'NONE'
        distance = float('inf')
        atLevel = -1
        while queue:
            cell, a, b, level = queue.popleft()
            if nearest != 'NONE' and level > atLevel: break
            for dx, dy in directions:
                j, k = a + dx, b + dy
                if (COL_START <= j <= COL_END and
                    ROW_START <= k <= ROW_END and 
                    (j, k) not in visited):
                    currCity = cities[(j, k)]
                    queue.append((currCity, j, k, level + 1))
                    visited.add((j, k))
                    if currCity and (j, k) in cities:
                        nX, nY = coords[currCity]
                        if not nX == X and not nY == Y: continue
                        newDistance = findDistance(X, Y, nX, nY)
                        if not nearest:
                            nearest = currCity
                            distance = newDistance
                            atLevel = level
                        elif distance >= newDistance:
                            nearest = nearest if nearest < currCity else currCity
                            
        closest.append(nearest)
        
    return closest
            
if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    c = input().split()
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    q = input().split()
    for _ in range(tests):
        print(*closestStraightCity(c, x, y, q))