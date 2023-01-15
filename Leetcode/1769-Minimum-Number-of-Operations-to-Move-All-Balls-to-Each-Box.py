class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        size = len(boxes)
        answers = [0] * size
        
        for i in range(size):
            for j in range(size):
                if i != j and boxes[j] == '1':
                    answers[i] += abs(i - j)
                
        return answers