class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        original_color = image[sr][sc]
        
        if original_color == newColor:
            return image
            
        rows = len(image)
        cols = len(image[0])
        
        def dfs(r: int, c: int):
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != original_color:
                return
                
            image[r][c] = newColor
            
            dfs(r + 1, c)  
            dfs(r - 1, c)  
            dfs(r, c + 1)  
            dfs(r, c - 1)  
            
        dfs(sr, sc)
        
        return image