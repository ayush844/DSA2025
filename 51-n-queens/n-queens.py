class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for _ in range(n)]
        results = []

        def convert_board(board):
            return [''.join(row) for row in board]

        def is_valid(row, col, board):

            for i in range(row):
                if board[i][col]=='Q':
                    return False

            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == 'Q':
                    return False

            for i, j in zip(range(row, -1, -1), range(col, n)):
                if board[i][j] == 'Q':
                    return False

            return True

        def place_next_queen(board, row):
            if row == n:
                results.append(convert_board(board))
                return
            for col in range(n):
                if is_valid(row, col, board):
                    board[row][col] = 'Q'
                    place_next_queen(board, row+1)
                    board[row][col] = '.'

        place_next_queen(board, 0)
        
        return results