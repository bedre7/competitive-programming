def runCase():
    n = int(input())
    events = []

    for i in range(n):
        curr = list(map(int, input().split()))
        events.append(curr)
    
    events.sort(key=lambda x: x[0])
    
    cache = events[0]
    count = 0
    for i in range(1, n):
        if events[i][0] > cache[0] and events[i][1] < cache[1]:
            count += 1
        else:
            cache = events[i]

    return count

if __name__ == '__main__':
    print(runCase())