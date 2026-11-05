class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #look through rows
        
        for row in range(len(board)):

            seen = set()

            for col in range(len(board[row])):

                if (board[row][col]) != ".":
                    if (board[row][col]) in seen:
                        return False
                    else:
                        seen.add(board[row][col])

        #look through rows
        
        for col in range(len(board)):

            seen = set()

            for row in range(len(board[row])):

                if (board[row][col]) != ".":
                    if (board[row][col]) in seen:
                        return False
                    else:
                        seen.add(board[row][col])
        
        #look through 3x3
        seen = set()

        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                seen = set()

                for row in range(start_row, start_row + 3):
                    for col in range(start_col, start_col + 3):

                        if (board[row][col]) != ".":
                            if (board[row][col]) in seen:
                                return False
                            else:
                                seen.add(board[row][col])
        return True







