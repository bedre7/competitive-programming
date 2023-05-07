class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        isPrime = [True] * (right + 1)
        isPrime[0] = isPrime[1] = False
        
        i = 2
        while i <= right:
            if isPrime[i]:
                j = i * 2
                while j <= right:
                    isPrime[j] = False
                    j += i
                    
            i += 1

        primes = [i for i in range(len(isPrime)) if isPrime[i] and i >= left]
        
        pair = [-1, -1]
        diff = float('inf')
        for i in range(len(primes) - 1):
            if primes[i + 1] - primes[i] < diff:
                diff = primes[i + 1] - primes[i]
                pair = [primes[i], primes[i + 1]]
                
        return pair