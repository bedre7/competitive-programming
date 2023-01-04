class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        smallest = None
        smallest_index = -1
        
        def findDistance(a, b):
            return abs(a - x) + abs(b - y)
        
        for i, point in enumerate(points):
            a, b = point
            if a == x or b == y:
                curr_dist = findDistance(a, b)
                if smallest == None or curr_dist < smallest:
                    smallest = curr_dist
                    smallest_index = i

        return smallest_index