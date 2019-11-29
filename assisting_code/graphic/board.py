# https://stackoverflow.com/questions/22835289/how-to-get-tkinter-canvas-to-dynamically-resize-to-window-width
import tkinter as tk


class Board:
    def __init__(self):
        self.min_ = 5
        self.size = 450
        self.max_ = self.size + self.min_  # changeable, must be divisable by 2 and 9 for symmetry
        self.step_ = self.size // 9
        self.master = tk.Tk()
        self.lines = list()
        self.cv = tk.Canvas(self.master, width=self.max_, height=self.max_, bg='#fff')
        self.create_board()

    # draw boarder, sep lines and grey offsquares
    def create_board(self):
        self.lines.append(self.cv.create_line(self.min_, self.min_, self.min_, self.max_))
        self.lines.append(self.cv.create_line(self.max_, self.min_, self.max_, self.max_))
        self.lines.append(self.cv.create_line(self.min_, self.min_, self.max_, self.min_))
        self.lines.append(self.cv.create_line(self.min_, self.max_, self.max_, self.max_))

        color_offsquares = '#ccc'
        up = [self.size // 3, 0, 2 * self.size // 3, self.size // 3]
        left = [0, self.size // 3, self.size // 3, 2 * self.size // 3]
        right = [2 * self.size // 3, self.size // 3, self.size, 2 * self.size // 3]
        down = [self.size // 3, 2 * self.size // 3, 2 * self.size // 3, self.size]
        offsquares = [[coord + self.min_ for coord in lst] for lst in [up, left, right, down]]
        for offsquare in offsquares:
            self.cv.create_rectangle(*offsquare, fill=color_offsquares)  # offsquares

        split = range(self.min_, self.max_, self.step_)
        for i in split:
            self.lines.append(self.cv.create_line(self.min_, i, self.max_, i))
            self.lines.append(self.cv.create_line(i, self.min_, i, self.max_))  # seplines

    '''
    Choose Later for Blinking Tile*
    
    def create_tile(self, i, j):
        color = ''
        if i in range(3, 6) != j in range(3, 6):
            color = '#f01'  # red
        else:
            color = '#0f2'  # green

        def coords(i, j):
            return j*self.step_, i*self.step_, j*self.step_ + self.step_, i*self.step_ + self.step_
        self.cv.create_rectangle(*coords(i, j), fill=color)
    '''

    # places numbers in cells
    def read_in(self, sudoku):
        for i in range(9):
            for j in range(9):
                if sudoku[i][j] != 0:
                    self.cv.create_text(j * self.step_ + self.step_ // 2 + self.min_,
                                        i * self.step_ + self.step_ // 2 + self.min_,
                                        fill="#000", font=f"Arial {self.size // 15} bold",
                                        text=str(sudoku[i][j]))

    # prints sudoku
    def showoff(self):
        self.cv.pack()
        self.master.mainloop()

    def postscript(self, path):
        self.cv.pack()
        self.master.mainloop()
        self.cv.update()
        self.cv.postscript(file=path, colormode='color')
        self.cv.mainloop()
