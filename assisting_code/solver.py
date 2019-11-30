import numpy as np

from assisting_code.board import Board


class solver:
    def __init__(self, sudoku):
        self.gamelog = []
        self.sudoku_init = self.transform(sudoku)
        self.game = Board(self.sudoku_init)

    def solve(self):
        sudoku = self.sudoku_init
        self.recurse(sudoku, 0, 0)

    def transform(self, s):
        s_ = ''.join([x for x in s if x.isdigit()])
        return [[int(num) for num in s_[i:i + 9]] for i in range(0, 81, 9)]

    def recurse(self, sudoku, i, j):
        if np.count_nonzero(sudoku) == 81:
            self.game.showoff(self.gamelog, sudoku)
            return True
        elif sudoku[i][j] == 0:
            poss = self.possibles(sudoku, i, j)
            if len(poss) == 0:
                sudoku[i][j] = 0
                return False
            else:
                for tries in poss:
                    sudoku[i][j] = tries
                    self.gamelog.append([j, i, sudoku[i][j], True])
                    if self.recurse(sudoku, *(self.indexhelp(i, j))):
                        return True
                    else:
                        self.gamelog.append([j, i, sudoku[i][j], False])
                        sudoku[i][j] = 0
        else:
            return self.recurse(sudoku, *(self.indexhelp(i, j)))

    def indexhelp(self, i, j):
        return (i + 1, 0) if j == 8 else (i, j + 1)

    def possibles(self, sudoku, row, col):
        rowT = list(np.transpose(sudoku)[col])
        col_min = (col // 3) * 3
        row_min = (row // 3) * 3
        sqaureofref = [sudoku[i][j] for i in range(row_min, row_min + 3) for j in
                       range(col_min, col_min + 3)]  # sudokusquare
        blocked_nums = list(set(sudoku[row] + rowT + sqaureofref))
        return [num for num in range(1, 10) if num not in blocked_nums and num > 0]
