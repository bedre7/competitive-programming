class Solution:
    intRomanMap = {
        '1'       :   'I',
        '5'       :   'V',
        '10'      :   'X',
        '50'      :   'L',
        '100'     :   'C',
        '500'     :   'D',
        '1000'    :   'M',
        '4'       :   'IV',
        '9'       :   'IX',
        '40'      :   'XL',
        '90'      :   'XC',
        '400'     :   'CD',
        '900'     :   'CM'
    }
    
    def intToRoman(self, num: int) -> str:
        roman = ''
        strNum = str(num)
        length = len(strNum)
        for i in range(length):
            currNum = strNum[i] + '0' * (length - i - 1)
            if currNum[0] == '0': continue
            if currNum in self.intRomanMap:
                roman += self.intRomanMap[currNum]
            else:
                roman += self.divide(currNum)
                
        return roman
    
    def divide(self, num: str):
        if len(num) == 1: return self.onedigitRoman(int(num))
        
        allkeys = self.intRomanMap.keys()
        strDividers = filter(lambda x: len(x) == len(num) and int(x) <= int(num), allkeys)
        intDividers = [int(x) for x in strDividers]
        intDividers.sort(reverse = True)

        result = ''
        intNum = int(num)
        for divider in intDividers:
            quo = intNum // divider
            remainder = intNum % divider
            if remainder != intNum:
                intNum %= divider
                result += self.intRomanMap[str(divider)] * quo
                if intNum != 0: result += self.divide(str(intNum))
                break
        
        return result
        
    def onedigitRoman(self, onedigit: int):
        if onedigit in self.intRomanMap:
            return self.intRomanMap[str(onedigit)]
        if onedigit in range(1, 4):
            return 'I' * onedigit
        if onedigit in range(6, 9):
            return 'V' + 'I' * (onedigit % 5)
        return ''
        
            
            
            
       