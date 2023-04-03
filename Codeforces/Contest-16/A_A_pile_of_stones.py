from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    operations = input()
    added = 0
    for op in operations:
        if op == '+':
            added += 1
        else:
            if added > 0:
                added -= 1
    
    print(added)
if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()