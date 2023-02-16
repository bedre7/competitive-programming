def runCase():
    N, M = map(int, input().split())
    first = list(map(int, input().split())) 
    second = list(map(int, input().split())) 

    first.sort()
    second.sort()
    left = right = 0

    less = [0] * len(second)
    while left < len(first) and right < len(second):
        less[right] = left
        while left < len(first) and second[right] > first[left]:
            less[right] += 1
            left += 1
        right += 1
    
    while right < len(second):
        less[right] = left
        right += 1
    
    print(*less)

if __name__ == '__main__':
    runCase()