from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = defaultdict(int)
        
        for _, loser in matches:
            losers[loser] += 1
        
        answer = [[], []]
        answer[0] = list(set([winner for winner, _ in matches if winner not in losers]))
        answer[1] = [loser for _, loser in matches if losers[loser] == 1]
        answer[0].sort()
        answer[1].sort()
        
        return answer