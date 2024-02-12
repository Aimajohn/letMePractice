class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        everything = []
        for i in range(9):
            for j in range(9):
                k = board[i][j]
                if k != '.':
                    everything+=[(i, k), (k, j), (i//3, j//3, k)]
        return len(everything) == len(set(everything))
