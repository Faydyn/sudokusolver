import os
from assisting_code.systempaths import get_abs_path


path = get_abs_path()
rel_path = 'sudokus'
abs_file_path = os.path.join(path, rel_path)  # define independent path of sudokus
excluded = ['example_split.txt']


def rename_all():
    filelist = os.listdir(abs_file_path)
    filelist = [x for x in filelist if x not in excluded]
    for filename in filelist:
        filepath = os.path.join(abs_file_path, filename)
        with open(filepath) as f:
            sudoku = f.read()

        sudoku = [x for x in (list(sudoku)) if x.isdigit()]
        sudoku = [sudoku[i:i + 9] for i in range(0, 81, 9)]
        prt = '\n'.join([''.join(line) for line in sudoku])

        with open(filepath, "w") as f:
            f.write(prt)

rename_all()