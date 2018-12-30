from tkinter import *
from functools import partial
from ro.ubb.test.grid import Cell


class GUI(object):
    def __init__(self,master,grid1,grid2):
        self.frame = Frame(master)
        self.grid1=grid1
        self.grid2=grid2
        self.frame.pack()

    planes = 0
    current_cell = None
    rotation = 1
    rotated = False

    def build_grids(self):
        self.canvas1 = Canvas(self.frame,width=600,height=350)
        self.canvas1.pack(side=LEFT)
        for i in range(1,9):
            for j in range(1,9):
                self.canvas = Canvas(self.canvas1, width=75, height=50, bd=1, highlightthickness=1, highlightbackground="black")
                cell = Cell(i,j, "empty",self.canvas)
                self.grid1.add_cell(cell,self.canvas)
                enter_hover_event = partial(self.enter_hover,cell,self.canvas)
                self.canvas.bind('<Enter>',enter_hover_event)
                exit_hover_event = partial(self.exit_hover,cell,self.canvas)
                self.canvas.bind('<Leave>',exit_hover_event)
                self.canvas.grid(row = i, column=j, columnspan=1)

    def pressed(self,cell,coords,canvas,event):
        print("PLACED")
        self.grid1.print_cells()
        self.planes = self.planes+1
        for item in coords:
            cell = self.grid1.get_cell(item[0],item[1])
            self.grid1.update_cell(cell,"occupied")
            self.grid1.set_canvas(cell, "blue")
        canvas.unbind('<Button-1>')

    def rotate(self,cell,canvas,event):
        self.destroy_hover_plane(self.current_cell)
        self.rotation = self.rotation+1
        if(self.rotation > 4):
            self.rotation = 1
        args = self.create_hover_plane(self.current_cell)
        new_coords = args[1]
        canvas.unbind('<Button-1>')
        if args[0] == "green":
            click_event = partial(self.pressed,cell,new_coords,canvas)
            canvas.bind('<Button-1>',click_event)

    def enter_hover(self,cell,canvas,event):
        if self.planes < 2:
            self.current_cell = cell
            args = self.create_hover_plane(cell)
            if args[0] == "green":
                coords = args[1]
                click_event = partial(self.pressed,cell,coords,canvas)
                canvas.bind('<Button-1>', click_event)
                rotate_event = partial(self.rotate,cell,canvas)
                canvas.bind('<Button-3>', rotate_event)
            else:
                canvas.unbind('<Button-1>')
                canvas.unbind('<Button-3>')
        else:
            canvas.unbind('<Button-1>')
            canvas.unbind('<Button-3>')

    def exit_hover(self,cell,canvas,event):
        if self.planes <2:
            canvas.unbind('<Buton-3>')
            self.destroy_hover_plane(cell)

    def create_hover_plane(self, original_cell):
        x = original_cell.x
        y = original_cell.y
        if self.rotation == 1:
            coords = [[x,y],[x,y+1],[x,y+2],[x-1,y+1],[x-2,y],[x-2,y+1],[x-2,y+2],[x-3,y+1]]
        elif self.rotation == 2:
            coords = [[x,y],[x+1,y],[x+2,y],[x+1,y+1],[x+1,y+2],[x,y+2],[x+2,y+2],[x+1,y+3]]
        elif self.rotation == 3:
            coords = [[x,y],[x,y+1],[x,y+2],[x+1,y+1],[x+2,y],[x+2,y+1],[x+2,y+2],[x+3,y+1]]
        elif self.rotation == 4:
            coords = [[x,y],[x+1,y],[x+2,y],[x+1,y-1],[x+1,y-2],[x,y-2],[x+2,y-2],[x+1,y-3]]
        color = "green"
        for item in coords:
            try:
                cell = self.grid1.get_cell(item[0],item[1])
                if cell.status == "occupied":
                    color = "red"
            except KeyError:
                continue
        for item in coords:
            try:
                cell = self.grid1.get_cell(item[0],item[1])
                self.grid1.set_canvas(cell,color)
            except KeyError:
                    color = "red"
                    try:
                        for item in coords:
                            cell = self.grid1.get_cell(item[0],item[1])
                            self.grid1.set_canvas(cell,color)
                    except KeyError:
                        continue
                    continue
        return color,coords

    def destroy_hover_plane(self, original_cell):
        x = original_cell.x
        y = original_cell.y
        if self.rotation == 1:
            coords = [[x,y],[x,y+1],[x,y+2],[x-1,y+1],[x-2,y],[x-2,y+1],[x-2,y+2],[x-3,y+1]]
        elif self.rotation == 2:
            coords = [[x,y],[x+1,y],[x+2,y],[x+1,y+1],[x+1,y+2],[x,y+2],[x+2,y+2],[x+1,y+3]]
        elif self.rotation == 3:
            coords = [[x,y],[x,y+1],[x,y+2],[x+1,y+1],[x+2,y],[x+2,y+1],[x+2,y+2],[x+3,y+1]]
        elif self.rotation == 4:
            coords = [[x,y],[x+1,y],[x+2,y],[x+1,y-1],[x+1,y-2],[x,y-2],[x+2,y-2],[x+1,y-3]]
        for item in coords:
            try:
                cell = self.grid1.get_cell(item[0],item[1])
                if cell.status=="empty":
                    self.grid1.set_canvas(cell,"white")
                else:
                    self.grid1.set_canvas(cell, "blue")
            except KeyError:
                continue