class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        islands = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def bfs(r, c):
            q = []
            grid[r][c] = "0"
            q.append((r,c))

            while q:
                row, col = q.pop(0)
                for dr, dc in directions:
                    if (row + dr in range(rows)
                    and col + dc in range(cols) 
                    and grid[row + dr][col + dc] == "1"):
                        q.append((row + dr,col + dc))
                        grid[row + dr][col + dc] = "0"

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    bfs(row , col)
                    islands += 1
        return islands


        