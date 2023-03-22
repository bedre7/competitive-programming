class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        votes = collections.defaultdict(int)
        votes[persons[0]] = 1
        winner = persons[0]
        self.winners = [[winner, times[0]]]
        
        for i in range(1, len(persons)):
            votes[persons[i]] += 1
            if votes[persons[i]] >= votes[winner]:
                winner = persons[i]
            
            self.winners.append([winner, times[i]])

    def q(self, t: int) -> int:
        return self.binarySearch(t, 0, len(self.winners) - 1)
    
    def binarySearch(self, t, start, end, votes=0):
        if start > end: return votes
        mid = (start + end) // 2
        if self.winners[mid][1] == t:
            return self.winners[mid][0]
        elif self.winners[mid][1] < t:
            votes = self.winners[mid][0]
            return self.binarySearch(t, mid + 1, end, votes)
        return self.binarySearch(t, start, mid - 1, votes)

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)