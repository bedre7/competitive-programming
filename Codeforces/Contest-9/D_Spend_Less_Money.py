from collections import defaultdict, Counter
def runCase():
    n, k = map(int, input().split())
    now = list(map(int, input().split()))
    later = list(map(int, input().split()))

    pair = []
    for i in range(n):
        pair.append([now[i], later[i], now[i] - later[i]])
    
    pair.sort(key=lambda x: x[2])

    total = 0
    for i in range(n):
        if k > 0:
            total += pair[i][0]
            k -= 1
        else:
            total += min(pair[i][1], pair[i][0])

    print(total)
        
if __name__ == '__main__':
    runCase()