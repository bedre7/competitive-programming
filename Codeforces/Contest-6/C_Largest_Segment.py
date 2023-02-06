def runCase():
    n = int(input())
    coords = []

    for i in range(n):
        curr = list(map(int, input().split()))
        curr.append(i + 1)
        coords.append(curr)

    minx = 10_000_000_000
    maxy = -1
    for i in range(n):
        minx = min(minx, coords[i][0])
        maxy = max(maxy, coords[i][1])
    
    for x, y, i in coords:
        if x == minx and y == maxy:
            return i
    
    return -1

if __name__ == '__main__':
    print(runCase())