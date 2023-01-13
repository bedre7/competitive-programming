class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smallers = []
        greaters = []
        equals = 0
        
        for num in nums:
            if num < pivot:
                smallers.append(num)
            elif num > pivot:
                greaters.append(num)
            else:
                equals += 1
        
        output = []
        
        for num in smallers:
            output.append(num)

        for i in range(equals):
            output.append(pivot)
        
        for num in greaters:
            output.append(num)
        
        return output