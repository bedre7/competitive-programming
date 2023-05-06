class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0
        isPrime = [0] * n
        isPrime[0] = isPrime[1] = -1
        
        i = 2
        while i < n:
            if isPrime[i] == 0:
                j = 2 * i
                while j < n:
                    isPrime[j] = -1
                    j += i
                
            i += 1
        
        return isPrime.count(0)