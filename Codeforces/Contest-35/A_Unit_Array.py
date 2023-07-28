from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    array = list(map(int, input().split()))
    total = sum(array)
    neg = pos = 0
    for num in array:
        if num == -1: neg += 1
        elif num == 1: pos += 1
    
    if neg == 0: return print(0)
    moves = 0
    if neg > pos: 
        moves = (neg - n // 2)
        neg -= moves
    if neg % 2 != 0:
        moves += 1
    print(moves)

if __name__ == '__main__':
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()