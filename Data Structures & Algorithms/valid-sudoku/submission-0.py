from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        


        seen = set()

        for row in range(len(board)):
            for i in range(len(board)):
                if board[row][i] != '.':
                    if board[row][i] in seen: return False
                    seen.add(board[row][i])
            seen.clear()

        seen.clear()
        for col in range(len(board)):
            for i in range(len(board)):
                if board[i][col] != '.':
                    if board[i][col] in seen: return False
                    seen.add(board[i][col])
            seen.clear()
        


        for i in range(0,9,3):
            for j in range(0,9,3):
                seen.clear()


                for row in range(i,i+3):
                    for col in range(j,j+3):
                        if board[row][col] != '.':
                            if board[row][col] in seen : return False
                        seen.add(board[row][col])

        return True







