# to split files (like sudokus_raw/test.txt) into single sudokus
import os
from assisting_code.systempaths import get_abs_path


path = get_abs_path()
rel_path = 'sudokus'
srcfile = 'example_split.txt'
abs_file_path = os.path.join(path, rel_path)  # define independent path of sudokus


def create_new(newtitle, content):
    filename = f'{"".join([x.lower() for x in newtitle if x.isalnum()])}.txt'  # clear of whitespaces, etc
    savepath = os.path.join(abs_file_path, filename)  # must have different title, otherwise overwrites
    newfile = open(savepath, "w+", encoding="utf-8")
    newfile.write(content)
    newfile.close


with open(os.path.join(abs_file_path, srcfile), 'r', encoding="utf-8") as file:
    buffer = ''
    title = file.readline()
    for line in file:
        if any([c.isalpha() for c in line]):  # looks for chars, matches only 'separating lines'
            create_new(title, buffer)
            buffer = ''  # after buffer is saved to file with titlename, it gets reset, so it can store a new sudoku
            title = line
        else:
            buffer += line  # buffer fills with lines until a new title appears

    create_new(title, buffer)  # because no titel after last sudoku
