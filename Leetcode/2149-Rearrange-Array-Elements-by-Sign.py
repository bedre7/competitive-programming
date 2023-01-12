class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []
        
        for num in nums:
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)
        
        output = []
        for i in range(len(positives)):
            output.append(positives[i])
            output.append(negatives[i])
        
        return output
            