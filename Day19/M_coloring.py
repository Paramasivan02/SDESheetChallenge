class Solution:
    def graphColoring(self, graph: list[list[int]], m: int, n: int) -> bool:
        color = [0] * n
        
        def is_safe(node: int, current_color: int) -> bool:
            for neighbor in range(n):
                if graph[node][neighbor] == 1 and color[neighbor] == current_color:
                    return False
            return True
            
        def solve(node: int) -> bool:
            if node == n:
                return True
                
            for c in range(1, m + 1):
                if is_safe(node, c):
                    color[node] = c  
                    
                    if solve(node + 1):
                        return True
                        
                    color[node] = 0
                    
            return False
            
        return solve(0)