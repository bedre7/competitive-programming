class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        answer = defaultdict(lambda: inf)
        adj = defaultdict(list)
        indegree = defaultdict(int)
        richests = set([p for p in range(len(quiet))])
        quietness = {q: i for i, q in enumerate(quiet)}
        for a, b in richer:
            adj[a].append(b)
            richests.discard(b)
            indegree[b] += 1
        
        queue = deque(richests)
        while queue:
            curr = queue.popleft()
            answer[curr] = min(answer[curr], quiet[curr])
            for sub in adj[curr]:
                answer[sub] = min(answer[sub], quiet[sub], answer[curr])
                indegree[sub] -= 1
                if indegree[sub] == 0:
                    queue.append(sub)
        
        return [quietness[answer[r]] for r in range(len(quiet))]