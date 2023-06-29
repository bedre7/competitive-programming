#User function Template for python3
from collections import defaultdict, deque
class Solution:
    def findOrder(self,alien_dict, N, K):
        # code here
        adj = {char: set() for word in alien_dict for char in word}
        for i in range(1, len(alien_dict)):
            first, second = alien_dict[i - 1], alien_dict[i]
            itr = min(len(first), len(second))
            if first[:itr] == second[:itr] and len(first) > len(second): return ''
            for j in range(itr):
                if first[j] != second[j]:
                    adj[first[j]].add(second[j])
                    break
        
        visited, path, res = set(), set(), []
        def dfs(char):
            if char in path: return False
            if char in visited: return True
            
            visited.add(char)
            path.add(char)
            for child in adj[char]:
                if not dfs(child): return False
            path.remove(char)
            res.append(char)
            return True
        
        for char in adj:
            if not dfs(char): return ''

        return ''.join(reversed(res))