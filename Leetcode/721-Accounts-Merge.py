from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = defaultdict(str)
        emailOwner, rank = defaultdict(str), defaultdict(lambda: 1)
        for account in accounts:
            owner, emails = account[0], account[1:]
            for email in emails:
                emailOwner[email] = owner
                parent[email] = email
        
        def find(email):
            p = parent[email]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(e1, e2):
            p1, p2 = find(e1), find(e2)
            if p1 == p2: return
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
        
        for account in accounts:
            for i in range(1, len(account) - 1):
                union(account[i], account[i + 1])

        merged = defaultdict(list)
        for child, par in parent.items():
            merged[find(par)].append(child)

        res = []
        for emails in merged.values():
            curr = [emailOwner[emails[0]]]
            curr.extend(sorted(emails))
            res.append(curr)

        return res
        # DFS
        # graph = defaultdict(list)
        # for account in accounts:
        #     if account[1] not in graph: graph[account[1]] = []
        #     for i in range(1, len(account) - 1):
        #         graph[account[i]].append(account[i + 1])
        #         graph[account[i + 1]].append(account[i])
        
        # counted = set()
        # def dfs(curr, emails):
        #     for email in graph[curr]:
        #         if email not in counted:
        #             counted.add(email)
        #             emails.append(email)
        #             dfs(email, emails)
        
        # output = []
        # for account in accounts:
        #     current = [account[0]]
        #     emails = [account[1]]
        #     if account[1] not in counted:
        #         counted.add(account[1])
        #         dfs(account[1], emails)
        #         current.extend(sorted(emails))
        #         output.append(current)
        
        # return output