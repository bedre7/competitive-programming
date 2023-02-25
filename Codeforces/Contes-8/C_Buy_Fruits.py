from collections import defaultdict, Counter, deque
def runCase():
    n, m = map(int, input().split())
    prices = list(map(int, input().split()))
    prices.sort()
    tags = deque(prices)

    fruits = defaultdict(int)
    for _ in range(m):
        fruits[(input())] += 1
    
    fruits = dict(sorted(fruits.items(), key=lambda item: item[1], reverse=True))
    
    minPrice = maxPrice = 0
    for k, v in fruits.items():
        minPrice += tags.popleft() * v

    tags = deque(prices)

    for k, v in fruits.items():
        maxPrice += tags.pop() * v
    
    print(minPrice, maxPrice)

if __name__ == '__main__':
    runCase()