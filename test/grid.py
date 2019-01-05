class Grid(object):

    def __init__(self):
        self.cells = {}
        self.canvases = {}
        self.planes = []

    def get_cell_status(self,cell):
        return self.cells["{0}{1}".format(cell.x,cell.y)].status

    def get_cell(self,x,y):
        return self.cells["{0}{1}".format(x,y)]

    def set_cell_attacked(self,cell):
        cell.attacked = True

    def is_cell_head(self,cell):
        for plane in self.planes:
            if cell.x == plane.head[0] and cell.y == plane.head[1]:
                return 1,plane
        return 0,0

    def add_plane(self,plane):
        self.planes.append(plane)
        for item in plane.coords:
            self.cells["{0}{1}".format(item[0],item[1])].status = "occupied"

    def destroy_plane(self,plane):
        for item in plane.coords:
            cell = self.get_cell(item[0],item[1])
            self.set_canvas(cell,"gray")
            self.set_cell_attacked(cell)

    def set_canvas(self,cell,color):
        self.canvases["{0}{1}".format(cell.x,cell.y)].configure(background=color)

    def set_hit(self,cell):
        self.canvases["{0}{1}".format(cell.x,cell.y)].configure(background="green")

    def set_miss(self,cell):
        self.canvases["{0}{1}".format(cell.x,cell.y)].configure(background="black")

    def reveal_planes(self):
        for plane in self.planes:
            for item in plane.coords:
                self.canvases["{0}{1}".format(item[0],item[1])].configure(background="red")
            self.canvases["{0}{1}".format(plane.head[0],plane.head[1])].configure(background="yellow")

    def add_cell(self,cell,canvas):
            self.cells["{0}{1}".format(cell.x,cell.y)] = cell
            self.canvases["{0}{1}".format(cell.x,cell.y)] = canvas

    def update_cell(self,cell,new):
            self.cells["{0}{1}".format(cell.x,cell.y)].status = new

    def print_cells(self):
            print(self.cells)


class Cell(object):

        attacked = False

        def __init__(self,x,y,status,canvas):
                self.x = x
                self.y = y
                self.status = status
                self.canvas = canvas

class Plane(object):

        def __init__(self, coords, head):
            self.coords = coords
            self.head = head
