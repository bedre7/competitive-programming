class Solution:
    def interpret(self, command: str) -> str:
        output = ''
        temp = ''
        
        for token in command:
            if token == 'G':
                output += token
            else:
                temp += token
                
            if temp == '()':
                output += 'o'
                temp = ''
            elif temp == '(al)':
                output += 'al'
                temp = ''
                
                
        return output