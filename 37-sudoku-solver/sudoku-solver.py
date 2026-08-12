class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        boxes = [{} for _ in range(9)]
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]

        def getBox(row, col):
            return (row // 3) * 3 + col // 3

        # Build lookup tables
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = board[r][c]
                    box = getBox(r, c)

                    boxes[box][num] = True
                    rows[r][num] = True
                    cols[c][num] = True

        def solveBacktrack():

            # Find the empty cell with the fewest choices
            best_row = -1
            best_col = -1
            best_choices = None

            for r in range(9):
                for c in range(9):

                    if board[r][c] != '.':
                        continue

                    box = getBox(r, c)

                    choices = []

                    for num in '123456789':
                        if (num not in rows[r] and
                            num not in cols[c] and
                            num not in boxes[box]):
                            choices.append(num)

                    # No possible number → this branch is impossible
                    if not choices:
                        return False

                    # Keep the cell with minimum choices
                    if best_choices is None or len(choices) < len(best_choices):
                        best_choices = choices
                        best_row = r
                        best_col = c

                        # Can't do better than one choice
                        if len(choices) == 1:
                            break

                if best_choices is not None and len(best_choices) == 1:
                    break

            # No empty cells → solved
            if best_choices is None:
                return True

            r = best_row
            c = best_col
            box = getBox(r, c)

            for num in best_choices:

                # Place
                board[r][c] = num
                rows[r][num] = True
                cols[c][num] = True
                boxes[box][num] = True

                if solveBacktrack():
                    return True

                # Backtrack
                board[r][c] = '.'
                del rows[r][num]
                del cols[c][num]
                del boxes[box][num]

            return False

        solveBacktrack()