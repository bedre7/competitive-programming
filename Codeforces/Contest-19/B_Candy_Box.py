from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    candies = list(map(int, input().split()))
    occur = Counter(candies)
    occur = sorted(occur.items(), key=lambda x: x[1], reverse=True)
    counted = set()
    size = 0
    
    for _, count in occur:
        currCount = count
        while currCount in counted:
            currCount -= 1
        if currCount > 0:
            counted.add(currCount)
            size += currCount
    
    print(size)

if __name__ == '__main__':
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()