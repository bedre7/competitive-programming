class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7
        def myPow(x: float, n: int) -> float:
            if n == 0: return 1
            if n < 0:
                return 1 / (x * myPow(x, -n - 1)) % mod
            if n % 2 == 0:
                return myPow(x * x % mod, n / 2) % mod
            return x % mod * myPow(x, n - 1) % mod
        
        evens = myPow(5, math.ceil(n / 2)) % mod
        primes = myPow(4, n // 2) % mod
        
        return evens * primes % mod
