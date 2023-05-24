from collections import defaultdict, Counter, deque

def countTwos(x):
    count = 0
    while x > 0:
        if x % 2 == 0:
            count += 1
        else: break
        x /= 2
    
    return count

def runCase():
    n = int(input())
    array = list(map(int, input().split()))
    product = 1
    for a in array:
        product *= a
    
    having = countTwos(product)
    need = n - having
    if need == 0:
        print(0)
        return
    
    twos = []
    for i in range(2, n + 1, 2):
        twos.append(countTwos(i))
    twos.sort(reverse=True)
    found = 0
    operations = 0
    for t in twos:
        if found >= need: break
        found += t
        operations += 1
    
    print(operations if found >= need else -1)

if __name__ == '__main__':
    tests = int(input())
    # tests = 1
    for _ in range(tests):
        runCase()