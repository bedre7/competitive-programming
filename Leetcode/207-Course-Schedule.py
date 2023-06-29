from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Solution 1 -> with two hashsets
        # visited -> to keep track of the closed nodes
        # path -> to keep track of the courses in the current path(for cycle detection)
        # preReq = defaultdict(list)
        # for crs, pre in prerequisites:
        #     preReq[crs].append(pre)
        
        # visited, path = set(), set()
        # def dfs(course):
        #     if course in path: return False
        #     if course in visited: return True

        #     path.add(course)
        #     for pre in preReq[course]:
        #         if not dfs(pre): return False
        #     path.remove(course)
        #     visited.add(course)
        #     return True
        
        # for course in range(numCourses):
        #     if not dfs(course): return False
        
        # return True
        # Solution 2 -> using coloring technique
        WHITE, BLACK, GRAY = -1, 0, 1
        colors = defaultdict(lambda: WHITE)
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        def cyclic(course):
            colors[course] = GRAY
            for pre in graph[course]:
                if colors[pre] == GRAY:
                    return True
                if colors[pre] == WHITE and cyclic(pre):
                        return True
            colors[course] = BLACK
            
            return False
            
        for course in range(numCourses):
            if colors[course] == WHITE:
                if cyclic(course):
                    return False
            
        return True
