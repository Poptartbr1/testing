class Grid(object):

   cells = {}
   canvases = {}

   def get_cell_status(self,cell):
        return self.cells["{0}{1}".format(cell.x,cell.y)]

   def get_cell(self,x,y):
        return self.cells["{0}{1}".format(x,y)]

   def set_canvas(self,cell,color):
       self.canvases["{0}{1}".format(cell.x,cell.y)].configure(background=color)

   def add_cell(self,cell,canvas):
           self.cells["{0}{1}".format(cell.x,cell.y)] = cell
           self.canvases["{0}{1}".format(cell.x,cell.y)] = canvas

   def update_cell(self,cell,new):
           self.cells["{0}{1}".format(cell.x,cell.y)].status = new

   def print_cells(self):
           print(self.cells["{0}{1}".format(1,1)])
           print(self.cells)

class Cell(object):

        def __init__(self,x,y,status,canvas):
                self.x = x
                self.y = y
                self.status = status
                self.canvas = canvas