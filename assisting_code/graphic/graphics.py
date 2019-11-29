# printing always done in here / returned further.
import pandas as pd
from assisting_code.graphic import board as b


def printsudoku(sudoku):
    game = b.Board()
    game.read_in(sudoku)
    game.showoff()
    pass


# cli-version
def prtsudoku(sudoku):
    df = pd.DataFrame(sudoku)
    print(df.to_string(index=False, header=False))
    print('--------------------------')
    pass
