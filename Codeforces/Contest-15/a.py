import sys, threading
from collections import defaultdict, Counter

def runCase():
    string = input()
    lowers = 0
    uppers = 0
    for c in string:
        if c.islower():
            lowers += 1
        else:
            uppers += 1
    
    if lowers >= uppers:
        print(string.lower())
    else:
        print(string.upper())
        
if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()