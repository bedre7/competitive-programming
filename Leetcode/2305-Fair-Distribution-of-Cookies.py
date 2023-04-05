class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        unfairness = float('inf')
        n = len(cookies)

        def backtrack(children, start):
            nonlocal unfairness
            if start == len(cookies):
                unfairness = min(unfairness, max(children.values()))
                return 
            
            for child in range(1, k + 1):
                children[child] += cookies[start]
                backtrack(children, start + 1)
                children[child] -= cookies[start]
                    
        children = collections.defaultdict(int)
        children[1] = cookies[0]# for optimization...TLE
        backtrack(children, 1)
        
        return unfairness