class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def binaryToDecimal(n: str) -> int:
            result = 0
            for i in range(len(n)):
                result += int(n[i]) * (2 ** (len(n) - i - 1))

            return result
    
        return bin(binaryToDecimal(a) + binaryToDecimal(b))[2:]