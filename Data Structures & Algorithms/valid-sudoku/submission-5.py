class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row = i,j
        for i in range(len(board)):
            if board[i] == board[i-1]:
                return True
            return False