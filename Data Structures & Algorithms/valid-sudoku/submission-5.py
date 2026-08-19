class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        square_set = defaultdict(set)

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                
                if (num in row_set[r]) or (num in col_set[c]) or (num in square_set[(r // 3, c // 3)]):
                    return False
                
                row_set[r].add(num)
                col_set[c].add(num)
                square_set[(r // 3, c // 3)].add(num)
                    
        return True