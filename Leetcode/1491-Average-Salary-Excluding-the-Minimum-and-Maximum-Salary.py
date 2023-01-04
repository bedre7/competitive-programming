class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        size = len(salary)
        total = sum(salary[1:-1])
        return total / (size-2)