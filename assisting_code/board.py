# https://stackoverflow.com/questions/22835289/how-to-get-tkinter-canvas-to-dynamically-resize-to-window-width
import time
import pandas as pd
import tkinter as tk


class Board:
    def __init__(self, sudoku):
        self.animated = False
        self.delay = 0.01
        self.min_ = 5
        self.size = 450
        self.max_ = self.size + self.min_  # changeable, must be divisable by 2 and 9 for symmetry
        self.step_ = self.size // 9
        self.master = tk.Tk()
        self.lines = list()
        self.cv = tk.Canvas(self.master, width=self.max_, height=self.max_, bg='#fff')
        self.create_board()
        self.tile = self.cv.create_rectangle(self.min_, self.min_, self.min_ + self.step_, self.min_ + self.step_,
                                             fill='#0f2')
        self.readin(sudoku)

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

    def color_tile(self, b):
        return '#0f0' if b else '#f00'

    def animate(self, gamelog):
        indices = [lst[:2] for lst in gamelog]
        diffs = list(zip(indices[:-1], indices[1:]))
        distances = [((pair[1][0] - pair[0][0]) * self.step_, (pair[1][1] - pair[0][1]) * self.step_)
                     for pair in diffs]  # row,column -> y,x | swapped here
        start = indices[0]
        colorcode = [lst[3] for lst in gamelog]
        values = [lst[2] for lst in gamelog]
        nums = list()

        self.cv.move(self.tile, start[1], start[0])
        self.cv.update()

        for (x, y), b, num, (j, i) in zip(distances, colorcode, values, indices):
            time.sleep(self.delay) if b else time.sleep(self.delay*1.2)
            self.cv.move(self.tile, x, y)
            self.cv.itemconfigure(self.tile, fill=self.color_tile(b))  # Check colorcode, when num inserting works
            if b:
                nums.append(self.cv.create_text(j * self.step_ + self.step_ // 2 + self.min_,
                                                i * self.step_ + self.step_ // 2 + self.min_,
                                                fill="#000", font=f"Arial {self.size // 15} bold",
                                                text=str(num)))
            else:
                self.cv.delete(nums[-1])
                nums = nums[:-1]

            self.cv.update()

    # places numbers in cells
    def readin(self, sudoku):
        for i in range(9):
            for j in range(9):
                if sudoku[i][j] != 0:
                    self.cv.create_text(j * self.step_ + self.step_ // 2 + self.min_,
                                        i * self.step_ + self.step_ // 2 + self.min_,
                                        fill="#000", font=f"Arial {self.size // 15} bold",
                                        text=str(sudoku[i][j]))
        self.cv.update()

    # prints sudoku
    def showoff(self, gamelog, end):
        self.cv.pack()
        if self.animated:
            self.cv.after(0, self.animate(gamelog))

        self.cv.update()
        self.cv.delete(self.tile)
        self.readin(end)
        self.master.mainloop()

    def prtsudoku(self, sudoku):
        df = pd.DataFrame(sudoku)
        print(df.to_string(index=False, header=False))
        pass
