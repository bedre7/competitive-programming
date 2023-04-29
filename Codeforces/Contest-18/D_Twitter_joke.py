from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    reposts = defaultdict(str)
    maxChain = 0

    posts = []
    for _ in range(n):
        reposter, _, owner = input().lower().split()
        if owner == 'polycarp':
            posts.append(reposter)
        reposts[owner] = reposter
    
    for post in posts:
        chain = 2
        while reposts[post]:
            post = reposts[post]
            chain += 1
        maxChain = max(maxChain, chain)
    
    print(maxChain)

if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()