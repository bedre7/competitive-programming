class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        matchings = 0
        pp = tp = 0
        
        while pp < len(players):
            while tp < len(trainers) and pp < len(players) and players[pp] > trainers[tp]:
                tp += 1
            if tp >= len(trainers): break
            tp += 1
            pp += 1
            matchings += 1
        
        return matchings