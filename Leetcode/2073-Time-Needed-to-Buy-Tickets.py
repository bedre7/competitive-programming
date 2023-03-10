class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        queue = collections.deque([[t, i] for i, t in enumerate(tickets)])
        
        while queue:
            queue[0][0] -= 1
            time += 1
            if queue[0][0] == 0:
                if queue[0][1] == k:
                    return time
                queue.popleft()
            else:
                queue.append(queue.popleft())
        
        return time
