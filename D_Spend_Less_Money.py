from collections import defaultdict, Counter
def runCase():
    n, k = map(int, input().split())
    now = list(map(int, input().split()))
    later = list(map(int, input().split()))

    pair = []
    for i in range(n):
        pair.append([now[i], later[i]])
    
    pair.sort(key=lambda x: x[0] - x[1])

    total = 0
    discounted = list(filter(lambda x: x[0] > x[1], pair))
    rest = list(filter(lambda x: x[0] <= x[1], pair))
    discounted.sort(key=lambda x: x[1] - x[0], reverse=True)
    print(discounted)
    count = 0
    for i in range(len(rest)):
        total += rest[i][0]
        rest[i][0] = -1
        count += 1
        
    for i in range(len(discounted)):
        if count >= k: break
        total += discounted[i][0]
        discounted[i][0] = -1
        count += 1

    for i in range(len(discounted)):
        if discounted[i][0] != -1:
            total += discounted[i][1] 

    print(total)
        
if __name__ == '__main__':
    runCase()