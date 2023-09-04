from collections import deque
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        dirs = [(0, 1), (1, 0), (1, 1), (-1, -1), (0, -1), (-1, 0), (1, -1), (-1, 1)]
        m, n = len(board), len(board[0])

        queue = deque([click])
visited = set([(click[0], click[1])])
        while queue:
            r, c = queue.popleft()
            visited.add((r, c))

            if board[r][c] == 'M':
                board[r][c] = 'X'
                break
            mines, toreveal = 0, []

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    if board[nr][nc] == 'M':
                        mines += 1
                    else:
                        toreveal.append((nr, nc))
            
            if board[r][c] == 'E':
                if mines > 0:
                    board[r][c] = str(mines)
                else:
                    board[r][c] = 'B'
                    queue.extend(toreveal)
        
        return board