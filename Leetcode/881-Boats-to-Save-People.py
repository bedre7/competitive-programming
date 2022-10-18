class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats, size = 0, len(people)
        heavier = size - 1
        lighter = 0
        while lighter <= heavier:
            if lighter == heavier:
                boats += 1
                break
            if people[lighter] + people[heavier] <= limit:
                heavier -= 1
                lighter += 1
            else:
                heavier -= 1
            boats += 1
        
        return boats
                
                
                