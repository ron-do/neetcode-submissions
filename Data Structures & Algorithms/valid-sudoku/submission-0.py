class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            checked = set()
            for col in range(9):
                if board[row][col] != ".":
                    if board[row][col] in checked:
                        return False
                    checked.add(board[row][col])
        
        for col in range(9):
            checked = set()
            for row in range(9):
                if board[row][col] != ".":
                    if board[row][col] in checked:
                        return False
                checked.add(board[row][col])

        for square in range(9):
            checked = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j

                    if board[row][col] != ".":
                        if board[row][col] in checked:
                            return False
                    checked.add(board[row][col])
        
        return True