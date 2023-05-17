from collections import defaultdict, Counter
def runCase():
    n = int(input())
    cost = list(map(int, input().split()))
    s_cost = sorted(cost)
    m = int(input())
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().split())))
    
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] += prefix[i - 1] + cost[i - 1]
    
    s_prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        s_prefix[i] += s_prefix[i - 1] + s_cost[i - 1]

    for type, left, right in queries:
        if type == 1:
            print(prefix[right] - prefix[left - 1])
        elif type == 2:
            print(s_prefix[right] - s_prefix[left - 1])

if __name__ == '__main__':
    runCase()