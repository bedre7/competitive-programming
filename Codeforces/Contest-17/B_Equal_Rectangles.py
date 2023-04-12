from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    for _ in range(n):
        recs = int(input())
        sides = deque(sorted(list(map(int, input().split()))))
        area = sides[0] * sides[-1]
        made = 0
        while len(sides) >= 2:
            if len(sides) % 4 == 0 and (sides[0] != sides[1] or sides[-1] != sides[-2]):
                print("NO")
                break
            a = sides.popleft()
            b = sides.pop()
            if a * b != area:
                print("NO")
                break
            made += 0.5
        else:
            if made != recs:
                print("NO")
            else: print("YES")

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()