class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ')':
                inner = ''
                while stack and stack[-1] != '(':
                    inner += stack.pop()
                stack.pop()
                for c in inner:
                    stack.append(c)
            else:
                stack.append(char)
        
        return ''.join(stack)