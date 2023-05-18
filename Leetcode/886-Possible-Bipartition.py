from collections import deque, defaultdict
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        
        colors = defaultdict(lambda: -1)
        def bfs(root):
            queue = deque([root])
            colors[root] = 1
            
            while queue:
                node = queue.popleft()
                for child in graph[node]:
                    if colors[child] == colors[node]:
                        return False
                    if colors[child] == -1:
                        colors[child] = 1 - colors[node]
                        queue.append(child)
                
            return True
        
        for person in range(1, n + 1):
            if colors[person] == -1:
                if not bfs(person):
                    return False
            
        return True