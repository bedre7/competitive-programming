from collections import defaultdict, Counter
def runCase():
    n = int(input())
    array = list(map(int, input().split()))
    coins = 0
    zeros = 0
    for a in array:
        if a == 0: 
            zeros += 1
            continue
        coins += abs(abs(a) - 1)
    
    neg = pos = 0
    for a in array:
        if a < 0: neg += 1
        else: pos += 1

    if neg % 2 == 1:
        if zeros > 0:
            coins += zeros
        else: coins += 2
    else:
        coins += zeros
        
    print(coins)

if __name__ == '__main__':
    runCase()