class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        valWeightMap = {}
        self.populateMap(items1, valWeightMap)
        self.populateMap(items2, valWeightMap)
        output = [[val, weight] for val, weight in valWeightMap.items()]
        
        output.sort(key=lambda n: n[0])
        return output
    def populateMap(self, items: List[List[int]], valWeightMap):
        for val, weight in items:
            if val in valWeightMap:
                valWeightMap[val] += weight
            else:
                valWeightMap[val] = weight