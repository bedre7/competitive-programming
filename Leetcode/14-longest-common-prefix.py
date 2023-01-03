class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ''
        
        for i in range(len(strs[0])):
            current_char = strs[0][i]
            for j in range(len(strs)):
                if i == len(strs[j]) or strs[j][i] != current_char:
                    return common_prefix
            
            common_prefix += current_char
        
        return common_prefix