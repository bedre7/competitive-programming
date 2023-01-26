class Solution:
    # With Bubble Sort
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(names) - 1):
            swapped = False
            for j in range(len(names) - i - 1):
                if heights[j] < heights[j + 1]:
                    heights[j], heights[j + 1] = heights[j + 1], heights[j]
                    names[j], names[j + 1] = names[j + 1], names[j]
                    swapped = True
            if not swapped:
                break
        
        return names
    
    # With Selection Sort
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        maxIndex = 0
        namesDict = {}
        
        for i in range(len(heights)):
            namesDict[heights[i]] = names[i]
        
        for i in range(len(heights)):
            maxHeightIndex = i
            for j in range(i, len(heights)):
                if heights[j] > heights[maxHeightIndex]:
                    maxHeightIndex = j

            heights[maxHeightIndex], heights[maxIndex] = heights[maxIndex],         heights[maxHeightIndex]
            
            maxIndex += 1
                
        return [namesDict[height] for height in heights]