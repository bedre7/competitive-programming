class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color == image[sr][sc]: return image
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(image), len(image[0])
        
        def dfs(r, c, COLOR):
            for dx, dy in dirs:
                x, y = r + dx, c + dy
                
                if (0 <= x < m and 0 <= y < n and
                   image[x][y] == COLOR):
                    image[x][y] = color
                    dfs(x, y, COLOR)
        
        dfs(sr, sc, image[sr][sc])
        image[sr][sc] = color
        
        return image