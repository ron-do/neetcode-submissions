class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        square_set = defaultdict(set)

        for row in range(9):
            for col in range(9):
                char = board[row][col]
                if char == ".":
                    continue

                if (char in row_set[row]) or \
                   (char in col_set[col]) or \
                   (char in square_set[(row // 3, col // 3)]):
                   return False

                row_set[row].add(char)
                col_set[col].add(char)
                square_set[(row // 3, col // 3)].add(char)

        return True