class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        isSafe = defaultdict(bool)

        def dfs(curr):
            if curr in isSafe: return isSafe[curr]
            isSafe[curr] = False
            for nei in graph[curr]:
                if not dfs(nei): return False
            isSafe[curr] = True
            return True

        safeOnes = []
        for node in range(len(graph)):
            if dfs(node):
                safeOnes.append(node)
        
        return safeOnes