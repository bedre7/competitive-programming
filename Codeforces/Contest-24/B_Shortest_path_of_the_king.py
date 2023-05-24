from collections import defaultdict, Counter, deque

def runCase():
    scoord = input()
    tcoord = input()
    s = [8 - int(scoord[1]), ord(scoord[0]) - 97]
    t = [8 - int(tcoord[1]), ord(tcoord[0]) - 97]
    dirs = [(1, 0), (0, 1), (1, 1), (0, -1), (-1, 0), (1, -1), (-1, 1), (-1, -1)]
    path = defaultdict(lambda: (-1, -1))

    trace = [(t[0], t[1])]
    def makepath(x, y):
        nonlocal trace
        while path[(x, y)] != (-1, -1):
            x, y = path[(x, y)]
            trace.append((x, y))
        trace = trace[::-1]
    
    queue = deque([s])
    visited = set()
    visited.add((s[0], s[1]))
    while queue:
        x, y = queue.popleft()
        if [x, y] == t:
            makepath(x, y)
            break
        for dx, dy in dirs:
            a, b = x + dx, y + dy
            if 0 <= a < 8 and 0 <= b < 8 and (a, b) not in visited:
                path[(a, b)] = (x, y)
                queue.append([a, b])
                visited.add((a, b))
    mmap = {
        (0, 1): 'R',
        (1, 0): 'D',
        (1, 1): 'RD',
        (0, -1): 'L',
        (-1, 0): 'U',
        (1, -1): 'LD',
        (-1, 1): 'RU',
        (-1, -1): 'LU'
    }
    print(len(trace) - 1)
    for i in range(len(trace) - 1):
        x, y = trace[i]
        a, b = trace[i + 1]
        print(mmap[(a - x, b - y)])

def main():
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()

if __name__ == '__main__':
    main()