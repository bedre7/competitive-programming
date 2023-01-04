class Solution:
    def freqAlphabets(self, s: str) -> str:
        temp = ''
        decoded = ''
        
        for char in s:
            if char.isdigit():
                if len(temp) < 2:
                    temp += char
                else:
                    decoded += chr(int(temp[0]) + 96)
                    temp = temp[1] + char
            else:
                decoded += chr(int(temp) + 96)
                temp = ''
        
        for char in temp:
            decoded += chr(int(char) + 96) 
        
        return decoded