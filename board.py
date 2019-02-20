class Board:  
    def __init__(self):
        self.cells = {}
    
    def add_cell(self,cell):
        self.cells["{0}{1}".format(cell.x,cell.y)] = cell
        
    def get_cell(self,coords):
        return self.cells[coords]
    
    def get_cell2(self,x,y):
        return self.cells["{0}{1}".format(x,y)]
    
    def get_empty_cell(self):
        for cell in self.cells.values():
            if cell.status == " ":
                return cell
        
    def update_cell(self,cell,status):
        self.cells["{0}{1}".format(cell.x,cell.y)].status = status
        
    def get_status(self,x,y):
        return self.cells["{0}{1}".format(x,y)].status
        
    def print_board(self):
        for i in range(1,4):
            print("+---+---+---+")
            row = self.get_row(i)
            print("|",row[0],"|",row[1],"|",row[2],"|")
        print("+---+---+---+")
                
    def get_row(self,i):
        row = []
        for j in range(1,4):
            row.append(self.cells["{0}{1}".format(i,j)].status)
        return row

class Cell:  
    def __init__(self,x,y,status):
        self.x=x
        self.y=y
        self.status = status