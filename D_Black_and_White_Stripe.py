def runCase():
    n, k = map(int, input().split())
    paper = input()

    blacks = 0
    for i in range(k):
        if paper[i] == 'B': 
            blacks += 1

    left = 1
    right = k

    maxBlacks = blacks
    while right < n:
        if paper[right] == 'B':
            blacks += 1
        if paper[left - 1] == 'B':
            blacks -= 1
        right += 1
        left += 1
        maxBlacks = max(maxBlacks, blacks)
    
    print(k - maxBlacks)

if __name__ == '__main__':
    tests = int(input())

    for _ in range(tests):
        runCase()