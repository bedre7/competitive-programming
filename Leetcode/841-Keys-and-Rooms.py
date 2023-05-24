from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)
        queue = deque([0])

        while queue:
            if len(visited) == len(rooms): return True
            curr = queue.popleft()
            for key in rooms[curr]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)
        
        return False

