from collections import defaultdict, Counter, deque
import sys
import threading
from functools import lru_cache

def runCase():
    n, m = map(int, input().split())
    members = []
    graph = defaultdict(list)
    for _ in range(n):
        members.append(input())
    for _ in range(m):
        a, b = input().split()
        graph[a].append(b)
        graph[b].append(a)

    counted = set()
    def bfs(person):
        nonlocal counted
        groups = [[], []]
        queue = deque([person])
        level = 0

        while queue:
            for _ in range(len(queue)):
                e = queue.popleft()
                groups[level].append(e)
                for f in graph[e]:
                    if f not in counted:
                        queue.append(f)
                        counted.add(f)

            level = 1 - level

        return groups[0] if len(groups[0]) > len(groups[1]) else groups[1]
    
    answer = []
    for i in range(n):
        if members[i] not in counted:
            counted.add(members[i])
            answer.extend(bfs(members[i]))

    answer.sort()
    print(len(answer))
    for p in answer:
        print(p)

def main():
    # tests = int(input())
    tests = 1
    for _ in range(tests):
        runCase()

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()