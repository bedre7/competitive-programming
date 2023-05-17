"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        total = 0
        emp = {e.id: e for e in employees}
        
        def dfs(current):
            nonlocal total
            total += current.importance
            
            for sub in current.subordinates:
                dfs(emp[sub])
        
        dfs(emp[id])
        return total