if __name__ == '__main__':
    n, l = map(int, input().split())

    lights = list(map(int, input().split()))

    lights.sort()

    maxDistance = lights[0]
    for i in range(len(lights) - 1):
        distance = lights[i + 1] - lights[i]
        maxDistance = max(maxDistance, distance)
    
    d = maxDistance / 2
    if lights[0] - d > 0:
        d = lights[0]
    
    if lights[-1] + d < l:
        d = l - lights[-1]
    
    print(d)