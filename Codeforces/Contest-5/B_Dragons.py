def solve():
    s, n = map(int, input().split())

    dragons = []
    for _ in range(n):
        dragons.append(list(map(int, input().split())))
    dragons.sort(key=lambda x: x[0])

    for strength, bonus in dragons:
        if s > strength:
            s += bonus
        else:
            print("NO")
            break
    else:
        print("YES")

if __name__ == '__main__':
    solve()