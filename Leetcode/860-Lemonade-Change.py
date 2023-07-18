class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = defaultdict(int)
        
        for bill in bills:
            if bill == 5:
                changes[bill] += 1
            elif bill == 10:
                changes[bill] += 1
                if changes[5] > 0: changes[5] -= 1
                else: return False
            else:
                if changes[5] > 0 and changes[10] > 0:
                    changes[5] -= 1
                    changes[10] -= 1
                elif changes[5] >= 3:
                    changes[5] -= 3
                else:
                    return False
        
        return True