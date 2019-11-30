import os
from PIL import Image
from assisting_code.board import Board
from assisting_code.solver import transform
from assisting_code.systempaths import get_abs_path

# Code doesnt error but also doesnt work
path_ = get_abs_path()
rel_path = 'sudokus'
subfolder = 'postscripts'
abs_file_path = os.path.join(path_, rel_path)
subf_path = os.path.join(abs_file_path, subfolder)
excluded = ['example_split.txt']

def ps_all():
    filelist = os.listdir(abs_file_path)
    filelist = [x for x in filelist if x not in excluded]
    for filename in filelist:
        filepath = os.path.join(abs_file_path, filename)
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
            sudoku = transform(content)
            b = Board()
            b.read_in(sudoku)

            def add_filetype(name,filetype):
                return f'{name[:-3]}.{filetype}'

            postscriptpath = os.path.join(subf_path, add_filetype(filename, 'ps'))  # try eps
            b.postscript(postscriptpath)
            img = Image.open(postscriptpath)
            img.save(os.path.join(abs_file_path, add_filetype(filename, 'png')))


ps_all()
