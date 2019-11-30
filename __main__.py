import sys
import tkinter as tk
from tkinter import filedialog
import os
from assisting_code.strings import English
from assisting_code.solver import solver
from assisting_code.systempaths import get_abs_path


def main():
    lang = English()
    print(lang.instruction())  # simple lang select (generalize & improve in strings)

    path = get_abs_path()
    rel_path = 'assisting_code/sudokus'
    abs_file_path = os.path.join(path, rel_path)  # define independent path of sudokus

    root = tk.Tk()
    root.withdraw()
    root.update()
    root.filename = filedialog.askopenfilename(initialdir=abs_file_path, title="Select file",
                                               filetypes=(
                                                   ("text files", "*.txt"),
                                                 ("all files", "*.*'")))
    root.update()
    root.destroy()
    # GUI for fileselction (askopenfilename muss be sandwich bei update, withdraw before!)

    with open(root.filename, 'r', encoding="utf-8") as file:
        sudoku = file.read()
        solver(sudoku).solve()  # read txt and give it to solver

    return


if __name__ == '__main__':
    main()
    sys.exit()

