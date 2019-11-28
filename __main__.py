from tkinter import filedialog
from tkinter import *
import os
from assisting_code.strings import English
from assisting_code.solver import solve
from assisting_code.systempaths import get_abs_path


def main():
    lang = English()
    print(lang.instruction())  # simple lang select (generalize & improve in strings)

    path = get_abs_path()
    rel_path = 'assisting_code/sudokus'
    abs_file_path = os.path.join(path, rel_path)  # define independent path of sudokus

    root = Tk()
    root.filename = filedialog.askopenfilename(initialdir=abs_file_path, title="Select file",
                                               filetypes=(
                                                   ("text files", "*.txt"),
                                                   ("all files", "*.*")))  # GUI for fileselction

    with open(root.filename, 'r', encoding="utf-8") as file:
        sudoku = file.read()
        solve(sudoku)  # read txt and give it to solver


if __name__ == '__main__':
    main()
    pass
