import sys, threading
from collections import defaultdict, Counter

def runCase():
    n = int(input())

    count = 0
    def convert(num):
        nonlocal count
        total = 0
        for c in num:
            total += int(c)

        if total > 9:
            count += 1
            convert(str(total))
    
    convert(str(n))
    print(count + (1 if n > 9 else 0))

def main():
    runCase()

if __name__ == '__main__':
    main()