from collections import deque
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        queue = deque(skill)
        
        teams = [[queue.popleft(), queue.pop()]]
        total = sum(teams[0])
        while queue:
            team = [queue.popleft(), queue.pop()]
            if sum(team) != total:
                return -1
            
            teams.append(team)
        
        chemistry = 0
        for l, r in teams:
            chemistry += l * r
        
        return chemistry