from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    matches = list(map(int, input().split()))
    k = sum(matches) // n
    moves = 0
    for match in matches:
        if match > k:
            moves += match - k
    
    print(2 * moves)

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()