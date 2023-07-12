class Solution:
    def __init__(self):
        self.mapping = defaultdict(list)
        # [[UP], [RIGHT], [DOWN], [LEFT]]
        self.mapping[1] = [[], [1, 3, 5], [], [1, 4, 6]]
        self.mapping[2] = [[2, 3, 4], [], [2, 5, 6], []]
        self.mapping[3] = [[], [], [2, 5, 6], [1, 4, 5]]
        self.mapping[4] = [[], [1, 3, 5], [2, 5, 6], []]
        self.mapping[5] = [[2, 3, 4], [], [], [1, 4, 6]]
        self.mapping[6] = [[2, 3, 4], [1, 3, 5], [], []]

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        par, m, n = defaultdict(tuple), len(grid), len(grid[0])
        
        def areConnected(i, j, k, l):
            if j == l: index = UP if i - k == 1 else DOWN
            if i == k: index = LEFT if j - l == 1 else RIGHT
            return grid[k][l]  in self.mapping[grid[i][j]][index]
        
        visited = set()
        def dfs(x, y):
            if x == m - 1 and y == n - 1: return True
            visited.add((x, y))
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if (0 <= nx < m and 0 <= ny < n and
                    (nx, ny) not in visited and areConnected(x, y, nx, ny)):
                    if dfs(nx, ny): return True
            return False
            
        return dfs(0, 0)