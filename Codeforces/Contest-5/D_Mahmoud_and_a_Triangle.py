def solve():
    n = int(input())

    sides = list(map(int, input().split()))
    sides.sort()

    for i in range(n-2):
        if sides[i] + sides[i+1] > sides[i+2]:
            print('YES')
            break
    else:
        print('NO')

if __name__ == '__main__':
    solve()