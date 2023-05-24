
class Solution:
    def isValid(self, s: str) -> bool:
        parMap = {')': '(', '}': '{', ']': '['}
        stack = []
        opening = ['(', '[', '{']
        closing = [')', ']', '}']
        
        for char in s:
            if char in opening:
                stack.append(char)
            elif char in closing:
                if not stack: return False
                if stack[-1] == parMap[char]:
                    stack.pop()
                else: return False
        
        return not stack