from collections import defaultdict
def solution():
    test_cases = int(input())
    cost1 = 1

    for _ in range(test_cases):
        n, cost2 = map(int, input().split())
        planets = input().split()

        orbit_map = defaultdict(int)
        for planet in planets:
            orbit_map[planet] += 1
        
        min_cost = 0
        for orbit in orbit_map.values():
            if cost2 < orbit * cost1:
                min_cost += cost2
            else:
                min_cost += orbit * cost1
        
        print(min_cost)

solution()
