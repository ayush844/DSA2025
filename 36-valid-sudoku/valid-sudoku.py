class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row_hash = {}
        col_hash = {}
        box_hash = {}

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if i in row_hash:
                        if board[i][j] in row_hash[i]:
                            return False
                        else:
                            row_hash[i].add(board[i][j])
                    else:
                        row_hash[i] = set([board[i][j]])

                    if j in col_hash:
                        if board[i][j] in col_hash[j]:
                            return False
                        else:
                            col_hash[j].add(board[i][j])
                    else:
                        col_hash[j] = set([board[i][j]])

                    box_key = str(i//3) + 'X' + str(j//3)
                    if box_key in box_hash:
                        if board[i][j] in box_hash[box_key]:
                            return False
                        else:
                            box_hash[box_key].add(board[i][j])
                    else:
                        box_hash[box_key] = set([board[i][j]])

                    

        return True