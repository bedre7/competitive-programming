class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num == 0:
            return [-1, 0, 1]
        
        if num < 3:
            return []
        
        num -= 3
        if num % 3 != 0:
            return []
        
        n = num // 3
        return [n, n + 1, n + 2]