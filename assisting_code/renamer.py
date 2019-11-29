import os
from assisting_code.systempaths import get_abs_path


path = get_abs_path()
rel_path = 'sudokus'
abs_file_path = os.path.join(path, rel_path)  # define independent path of sudokus
excluded = ['example_split.txt']


def rename_all():
    filelist = os.listdir(abs_file_path)
    filelist = [x for x in filelist if x not in excluded]
    for i, filename in enumerate(filelist):
        old = os.path.join(abs_file_path, filename)
        new = os.path.join(abs_file_path, f'sudoku{i:03d}.txt')
        os.rename(old, new)


rename_all()