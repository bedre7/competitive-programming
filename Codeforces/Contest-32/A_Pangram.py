from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    word = input().lower()
    if len(set(word)) == 26: print("YES")
    else: print("NO")


if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()
