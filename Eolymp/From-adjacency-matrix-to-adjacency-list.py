from collections import defaultdict, Counter, deque

def runCase():
    n = int(input())
    graph = defaultdict(list)

    for i in range(n):
        line = list(map(int, input().split()))
        for j, v in enumerate(line):
            if v == 1:
                graph[i + 1].append(j + 1)
    
    for k, v in sorted(graph.items(), key=lambda x: x[0]):
        print(len(v), *sorted(v))


if __name__ == '__main__':
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()