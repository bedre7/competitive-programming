def solution():
    n = int(input())
    points = list(map(int, input().split()))

    count = 0

    for i in range(1, n):
        isLess = points[i] < points[i - 1]
        for j in range(i - 1, -1, -1):
            if isLess:
                if points[i] >= points[j]:
                    break
            else:
                if points[i] <= points[j]:
                    break
        else:
            count += 1
            continue

    print(count)
                
solution()