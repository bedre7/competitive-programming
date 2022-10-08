class Solution:
    def sortAlphabetically(self, strs: list[str]) -> list[str]:
        strsCopy = []
        for string in strs: strsCopy.append(''.join(sorted(string))) 
        return strsCopy

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = {}
        answer = []

        strsCopy = self.sortAlphabetically(strs)
        for i in range(len(strsCopy)):
            if strsCopy[i] in anagrams:
                anagrams.get(strsCopy[i]).append(strs[i])
            else:
                anagrams[strsCopy[i]] = [strs[i]]

        for values in anagrams.values():
            answer.append(values)
        return answer

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

