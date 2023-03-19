class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(word):
            return sorted(Counter(word).items(), key=lambda item: item[0])[0][1]
        
        freq = []
        for word in words: 
            freq.append(f(word))
        
        freq.sort()
        def countAbove(base):
            start = 0
            end = len(freq) - 1
            
            firstBelow = None
            while start <= end:
                mid = (start + end) // 2
                if freq[mid] > base:
                    end = mid - 1
                elif freq[mid] <= base:
                    start = mid + 1
                    firstBelow = mid
            
            if firstBelow == None: return len(freq)
            return len(freq) - firstBelow - 1
        
        output = []
        for query in queries:
            queryCount = f(query)
            output.append(countAbove(queryCount))
            
        return output