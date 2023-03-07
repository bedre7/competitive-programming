from collections import defaultdict, Counter
def runCase():
    n, m, k = map(int, input().split())
    seats = []
    for _ in range(n):
        seats.append([c for c in input()])
    
    ans = 0
    for i in range(n):
        for j in range(m - k + 1):
            if '*' not in seats[i][j:j+k]:
                ans += 1
    
    reverse = []

    for i in range(n):
        for j in range(m):
            if len(reverse) <= j: reverse.append([])
            reverse[j].append(seats[i][j])

    for i in range(m):
        for j in range(n - k + 1):
            if '*' not in reverse[i][j:j+k]:
                ans += 1

    print(ans)

if __name__ == '__main__':
    runCase()