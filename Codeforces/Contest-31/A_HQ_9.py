from collections import defaultdict, Counter, deque

def runCase():
    code = set(input())
    if 'H' in code or 'Q' in code or '9' in code:
        print("YES")
    else:
        print("NO")
                    
if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()
