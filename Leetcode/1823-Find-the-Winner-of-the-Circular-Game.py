class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        loser = 0
        friends = [i + 1 for i in range(n)]
        
        while len(friends) > 1:
            loser = (loser + k - 1) % n
            friends.pop(loser)
            n -= 1
        
        return friends[0]