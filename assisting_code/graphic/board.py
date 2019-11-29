# https://stackoverflow.com/questions/22835289/how-to-get-tkinter-canvas-to-dynamically-resize-to-window-width
import tkinter as tk


class Board:
    def __init__(self):
        self.min_ = 0
        self.max_ = 900
        self.step_ = self.max_ // 9
        self.master = tk.Tk()
        self.lines = list()
        self.cv = tk.Canvas(self.master, width=self.max_, height=self.max_, bg='#fff')
        self.create_board()

    # draw sep lines and grey offsquares
    def create_board(self):
        color_offsquares = '#bbb'
        self.cv.create_rectangle(self.max_ // 3, self.min_, 2 * self.max_ // 3, self.max_ // 3, fill=color_offsquares)
        self.cv.create_rectangle(self.min_, self.max_ // 3, self.max_ // 3, 2 * self.max_ // 3, fill=color_offsquares)
        self.cv.create_rectangle(2 * self.max_ // 3, self.max_ // 3, self.max_, 2 * self.max_ // 3,
                                 fill=color_offsquares)
        self.cv.create_rectangle(self.max_ // 3, 2 * self.max_ // 3, 2 * self.max_ // 3, self.max_,
                                 fill=color_offsquares)

        split = range(self.min_, self.max_, self.step_)
        for i in split:
            self.lines.append(self.cv.create_line(self.min_, i, self.max_, i))
            self.lines.append(self.cv.create_line(i, self.min_, i, self.max_))

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
                self.cv.create_text(j * self.step_ + self.step_ // 2, i * self.step_ + self.step_ // 2,
                                    fill="#000", font="Arial 48 bold", text=str(sudoku[i][j]))

    # prints sudoku
    def showoff(self):
        self.cv.pack()
        self.master.mainloop()
        self.cv.destroy()


