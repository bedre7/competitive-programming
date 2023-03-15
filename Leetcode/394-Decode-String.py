class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        k = ''
        decoded = ''
        for i in range(len(s)):
            if s[i] == '[':
                stack.append(decoded)
                stack.append(int(k))
                k = decoded = ''
            elif s[i].isdigit():
                k += s[i]
            elif s[i] == ']':
                num = stack.pop()
                string = stack.pop()
                decoded = string + decoded * num
            else:
                decoded += s[i]
            
        return decoded