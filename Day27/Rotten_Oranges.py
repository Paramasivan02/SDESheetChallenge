from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0
            
        rows = len(grid)
        cols = len(grid[0])
        
        queue = deque()
        fresh_count = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh_count += 1
                    
        if fresh_count == 0:
            return 0
            
        max_time = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            r, c, time = queue.popleft()
            
            max_time = max(max_time, time)
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_count -= 1
                    
                    queue.append((nr, nc, time + 1))
                    
        return max_time if fresh_count == 0 else -1