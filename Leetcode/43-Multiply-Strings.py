class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        rows = []
        prodSize = len(num1) + len(num2)
        temp = prodSize
        
        for a in num2[::-1]:
            product = [''] * (prodSize)
            index = temp - 1
            carry = 0
            for b in num1[::-1]:
                result = int(a) * int(b) + carry
                carry = result // 10
                result %= 10
                product[index] = str(result)
                index -= 1
            if carry != 0:
                product[index] = str(carry)
            temp -= 1
            rows.append(product)
        
        print(rows)
        return ''.join(self.addRows(rows))
        
    def addRows(self, rows: List[List[str]]):
        result = [''] * len(rows[0])
        
        carry = 0
        for i in range(len(rows[0]) - 1, -1, -1):
            res = 0
            for j in range(len(rows)):
                if rows[j][i] == '':
                    continue
                res += int(rows[j][i])
            res += carry
            carry = res // 10
            res %= 10
            result[i] = str(res)
        
        if result[0] == "0":
            result = result[1:]
        if carry != 0:
            result.insert(0, str(carry))
        
        return result