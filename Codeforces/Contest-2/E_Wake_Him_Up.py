def wake_him_up(n, k, theorems, behavior):
    obvious_theorems = 0

    for i in range(n):
        if behavior[i] == 1:
            obvious_theorems += theorems[i]
    
    awoken = 0
    for i in range(k):
        if behavior[i] == 0:
            awoken += theorems[i]
    
    max_notes = awoken
    for right in range(k, n):
        left = right - k
        if behavior[left] == 0:
            awoken -= theorems[left]
        if behavior[right] == 0:
            awoken += theorems[right]
        
        max_notes = max(max_notes, awoken)
    
    print(max_notes + obvious_theorems)


if __name__ == '__main__':
    n, k = map(int, input().split())
    theorems = list(map(int, input().split()))
    behavior = list(map(int, input().split()))

    wake_him_up(n, k, theorems, behavior)