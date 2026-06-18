class Solution:
    def solveSudoku(self, board: list[list[str]]):

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []
        
        for r in range(9):
            for c in range(9):
                if str(board[r][c]) == '.':
                    empty_cells.append((r, c))
                else:
                    val = str(board[r][c])
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + c // 3].add(val)
                    
        def solve(index: int) -> bool:
            if index == len(empty_cells):
                return True
                
            r, c = empty_cells[index]
            box_idx = (r // 3) * 3 + c // 3
            
            for val in '123456789':
                if val not in rows[r] and val not in cols[c] and val not in boxes[box_idx]:
                    board[r][c] = val
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_idx].add(val)
                    
                    if solve(index + 1):
                        return True
                        
                    board[r][c] = '.'
                    rows[r].remove(val)
                    cols[c].remove(val)
                    boxes[box_idx].remove(val)
                    
            return False
            
        solve(0)
        
        return board