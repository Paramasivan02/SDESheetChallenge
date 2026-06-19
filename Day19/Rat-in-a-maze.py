class Solution:
    def findPath(self, m: list[list[int]], n: int) -> list[str]:
        if m[0][0] == 0 or m[n - 1][n - 1] == 0:
            return []
            
        ans = []
        directions = [(1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R'), (-1, 0, 'U')]
        
        def solve(r: int, c: int, path: str):
            if r == n - 1 and c == n - 1:
                ans.append(path)
                return
            
            m[r][c] = 0
            
            for dr, dc, move in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < n and 0 <= nc < n and m[nr][nc] == 1:
                    solve(nr, nc, path + move)
            
            m[r][c] = 1
            
        solve(0, 0, "")
        return ans