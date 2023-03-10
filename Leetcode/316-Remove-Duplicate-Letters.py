class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        occur = {c: i for i, c in enumerate(s)}
        stack = []
        seen = set()
        
        for i, char in enumerate(s):
            if char not in seen:
                while stack and stack[-1] > char and occur[stack[-1]] > i:
                    last = stack.pop()
                    seen.remove(last)
                stack.append(char)
                seen.add(char)

        return ''.join(stack)