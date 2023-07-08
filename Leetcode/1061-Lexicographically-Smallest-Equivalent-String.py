class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = defaultdict(str)
        for i in range(ord('a'), ord('z') + 1):
            parent[chr(i)] = chr(i)

        def find(char):
            p = parent[char]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        def union(c1, c2):
            p1, p2 = find(c1), find(c2)
            if p1 == p2: return
            if p1 < p2:
                parent[p2] = p1
            else:
                parent[p1] = p2
        
        for i in range(len(s1)):
            union(s1[i], s2[i])
        
        equivStr = []
        for char in baseStr:
            equivStr.append(find(char))
        
        return ''.join(equivStr)