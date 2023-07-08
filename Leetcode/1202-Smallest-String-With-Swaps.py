class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # Union Find
        parent = [i for i in range(len(s))]

        def find(char):
            p = parent[char]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(c1, c2):
            p1, p2 = find(c1), find(c2)
            if p1 == p2: return
            parent[p2] = p1
        
        for a, b in pairs:
            union(a, b)
        
        components = defaultdict(list)
        for i in range(len(s)):
            components[find(i)].append(s[i])
        for par in components.keys():
            components[par].sort(reverse=True)
        swapped = []
        for i in range(len(s)):
            swapped.append(components[find(i)].pop())
        return ''.join(swapped)
        # DFS
        # graph = defaultdict(list)
        # for u, v in pairs:
        #     graph[u].append(v)
        #     graph[v].append(u)
        
        # visited = set()
        # component = set()
        # string = []
        # def dfs(u):
        #     for v in graph[u]:
        #         if v not in visited:
        #             visited.add(v)
        #             component.add(v)
        #             string.append(s[v])
        #             dfs(v)
        
        # outputStr = [c for c in s]
        # for u, v in pairs:
        #     if u not in visited:
        #         visited.add(u)
        #         string = [s[u]]
        #         component.clear()
        #         component.add(u)
        #         dfs(u)
        #         indices = sorted(list(component))
        #         sortedStr = sorted(''.join(string))
        #         i = 0
        #         for c in sortedStr:
        #             outputStr[indices[i]] = c
        #             i += 1
        
        # return ''.join(outputStr)