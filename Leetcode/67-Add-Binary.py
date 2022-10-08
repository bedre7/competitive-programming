class Solution:
    def decimalToBinary(self, n: int, result = '') -> str:
        if(n >= 1):
            return self.decimalToBinary(n//2, result + '0') if n % 2 == 0 else self.decimalToBinary(n//2, result + '1')
        return result[::-1]

    def binaryToDecimal(self, n: str) -> int:
        result = 0
        for i in range(len(n)):
            temp = int(n[i]) * (2 ** (len(n) - i - 1))
            if temp == 0:
                continue
            result += temp
        return result

    def addBinary(self, a: str, b: str) -> str:
        if a == '0' and b == '0':
            return "0"
        return self.decimalToBinary(self.binaryToDecimal(a) + self.binaryToDecimal(b))