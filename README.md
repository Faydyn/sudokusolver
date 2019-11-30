# sudokusolver
Python Programm to solve any Sudoku via Backtracking
###### by faydyn
___
[Sudoko Backtracking](sodbtff.gif)
___
### WiP (Branch: graphic)
##### Latest Update: 2019-11-29
* Implement fast or graphical solution - decider
* Language Superclass / languages as subclasses
___
### Needs Fixing
* "spaced" sudokus to non-spaced
* weird offset on blinking tile (seems to be the read in Sudoku with Spaces)
* not enough delay async numbers and color tile
___
### Development Plans
* ~py2exec to run on other PCs
___
### Releases
##### v0.1 (2019-11-28)
* __Backtracking Algorithm__ implemented working (without optimizations)
* __Parser__ for .txt-Files to read multiple Sudokus (separated by some alphabetical char (title))
* __os-package__ absolute pathes working  ($\Rightarrow$ should be working in every folder on every system)
* __Tkinter__ GUI (simple, to choose sudoku to solve)
* __Tkinter__ graphical solution + animation
* Board resizeable and offsetable