from typing import List
from collections import defaultdict
class Solution:
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        WHITE, GRAY, BLACK = -1, 0, 1
        colors = defaultdict(lambda: WHITE)
	    
        def cyclic(curr, parent):
            colors[curr] = GRAY
            for nei in adj[curr]:
                if nei == parent: continue
                if colors[nei] == GRAY or cyclic(nei, curr): return True
            colors[curr] = BLACK
            return False
		    
        for node in range(V):
            if colors[node] == WHITE:
                if cyclic(node, -1): return True
		      
        return False