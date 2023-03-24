class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(key=lambda x: x[0], reverse=True)
        
        times = []
        for i in range(len(cars)):
            times.append((target - cars[i][0]) / cars[i][1])
        
        print(times)
        fleets = slowest = 0
        
        for i in range(len(times)):
            if times[i] > slowest:
                fleets += 1
                slowest = times[i]
        
        return fleets