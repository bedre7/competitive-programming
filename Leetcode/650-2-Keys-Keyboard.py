class Solution:
    def minSteps(self, n: int) -> int:
        steps = 0
        f = 2
        while n > 1:
            while n % f == 0:
                steps += f
                n /= f
            f += 1
            
        return steps