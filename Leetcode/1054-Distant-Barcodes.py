from collections import Counter
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        freqDict = dict(Counter(barcodes))
        freqDict = dict(sorted(freqDict.items(), key=lambda x: x[1], reverse=True))
        
        n = len(barcodes)
        output = [0] * n
                    
        i = 0
        for num, freq in freqDict.items():
            for j in range(freq):
                output[i] = num
                i += 2
                if i >= n:
                    i = 1
        
        return output