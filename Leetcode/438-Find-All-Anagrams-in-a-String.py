class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        indices = []
        pCount, sCount = {}, {}
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
        
        left = 0
        for right in range(len(p), len(s) + 1):
            for key, val in pCount.items():
                if sCount.get(key, 0) != val:
                    break
            else:
                indices.append(left)
            sCount[s[left]] -= 1
            if right == len(s): break
            sCount[s[right]] = 1 + sCount.get(s[right], 0)
            left += 1
            
        return indices