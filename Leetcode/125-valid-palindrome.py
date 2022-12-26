import re
class Solution:
    def filter(self, s: str) -> str:
        filteredStr = ''
        for c in s:
            if re.search("[a-z0-9A-Z]", c):
                filteredStr += c

        return filteredStr

    def isPalindrome(self, s: str) -> bool:
        finalStr = self.filter(s).lower()
        return finalStr == finalStr[::-1]