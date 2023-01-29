class Solution:
    def largestNumber(self, nums: List[int]) -> str:            
        strNums = list(map(str, nums))
        size = len(strNums)
        for i in range(size):
            for j in range(size - i - 1):
                if strNums[j] + strNums[j + 1] < strNums[j + 1] + strNums[j]:
                    strNums[j], strNums[j + 1] = strNums[j + 1], strNums[j]
        
        if strNums[0] == '0':
            return '0'
        
        return ''.join(strNums)