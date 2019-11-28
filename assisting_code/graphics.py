# printing always done in here / returned further.
import pandas as pd


def givesudoku(sudoku):
    df = pd.DataFrame(sudoku)
    print(df.to_string(index=False))
    pass
