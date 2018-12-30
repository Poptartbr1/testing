from tkinter import *
from ro.ubb.test.gui import GUI
from ro.ubb.test.grid import Grid


if __name__ == '__main__':
    root = Tk()
    grid = Grid()
    grid2 = Grid()
    gui = GUI(root,grid,grid2)
    root.geometry('1200x700')
    gui.build_grids()
    root.mainloop()
