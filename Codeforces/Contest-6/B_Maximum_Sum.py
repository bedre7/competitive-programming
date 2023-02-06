def runCase():
    n, m = map(int, input().split())
    tvs = list(map(int, input().split()))

    tvs.sort()

    money = 0
    for i in range(m):
        if tvs[i] < 0:
            money += -tvs[i]
    
    print(money)

if __name__ == '__main__':
    runCase()