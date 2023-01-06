class Solution:
    def removeComments(self, source: list[str]) -> list[str]:
        cleaned = ''
        
        code = '\n'.join(source) + '\n'
        size, i = len(code), 0 
        while i < size:
            if i + 1 < size and code[i] == '/' and code[i + 1] == '*':
                i = code.find('*/', i + 2) + 2
            elif i + 1 < size and code[i] == code[i + 1] == '/':
                i = code.find('\n', i + 2)
            else:
                cleaned += code[i]
                i += 1
        
        return list(filter(len, cleaned.split('\n')))