from collections import defaultdict, Counter, deque

def runCase():
    bracketes = input().strip()
    stack = []
    invalid = 0
    for b in bracketes:
        if b == '(':
            stack.append(b)
        else:
            if not stack: invalid += 1
            else: stack.pop()
    
    print(len(bracketes) - (len(stack) + invalid))

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()