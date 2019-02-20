from board import Cell
from random import randint

class Game:
    
    turn = 0
    game_phase = 0 #0 is placement 1 is movement
    
    def __init__(self,board):
        self.board = board
        
    def init_board(self):
        for i in range(1,4):
            for j in range(1,4):
                cell = Cell(i,j," ")
                self.board.add_cell(cell)
                
    def print_board(self):
        self.board.print_board()
    
    def save_game(self,name):
        file = open(name,"w")
        for i in range(1,4):
            for j in range(1,4):
                cell = self.board.get_cell2(i,j)
                file.write("{0}-{1}-{2}\n".format(cell.x, cell.y, cell.status))
        file.write(str(self.turn)+"\n")
        file.write(str(self.game_phase))
        
    
    def load_game(self,name):
        file = open(name, "r")
        lines = []
        for i in range(1,10):
            line = file.readline()
            lines.append(line)
        for l in lines:
            l.strip("\n")
            cell = Cell(int(l[0]),int(l[2]),l[4])
            self.board.update_cell(cell,l[4])
        self.turn = int(file.readline())
        self.game_phase = int(file.readline())
        if self.game_phase == 0:
            self.print_board()
            self.start_placement()
        else:
            self.print_board()
            self.start_movement()
      
    def start_placement(self):
        ended = False
        placed = 0
        while ended != True:
            if placed == 8:
                self.game_phase = 1
                print("Movement phase begins")
                self.start_movement()
                ended = True
                break
            if self.turn == 0:
                #player turn
                print("It's your turn, where do you want to place X?")
                valid_choices = ["11","12","13","21","22","23","31","32","33"]
                try:
                    player_choice = input("Choice: ")
                    if player_choice == "save":
                        name_file = input("File name: ")
                        self.save_game(name_file)
                    elif player_choice not in valid_choices:
                        raise Exception("Wrong input")
                    cell = self.board.get_cell(player_choice)
                    if cell.status != " ":
                        raise Exception("Cell already occupied")
                    self.board.update_cell(cell,"X")
                    placed = placed + 1
                    if self.check_win("X") == 1:
                        self.print_board()
                        print("YOU HAVE WON")
                        break
                    else:
                        self.turn = 1
                except Exception as er:
                    print(er)
            else:
                #Computer turn
                found_move = False
                while found_move == False:
                    best_move = self.can_player_win()
                    if best_move != 0:
                        found_move = True
                        self.board.update_cell(best_move,"O")
                        self.print_board()
                        self.turn = 0
                        break
                    move_x = randint(1,3)
                    move_y = randint(1,3)
                    move = move_x*10+move_y
                    cell = self.board.get_cell(str(move))
                    if cell.status == " ":
                        found_move = True
                        self.board.update_cell(cell,"O")
                        self.print_board()
                        print("Computer has placed an O on position ", move_x,move_y)
                        self.turn = 0
                        placed = placed+1
                if self.check_win("O") == 1:
                    print("Computer has WON")
                    break
                
    def start_movement(self):
        ended = False
        while ended == False:
            if self.turn == 0:
                print("What piece to move to the empty space")
                valid_choices = ["11","12","13","21","22","23","31","32","33"]
                try:
                    player_choice = input("Choice: ")
                    if player_choice == "save":
                        name_file = input("File name: ")
                        self.save_game(name_file)
                    elif player_choice not in valid_choices:
                        raise Exception("Wrong input")
                    empty_cell = self.board.get_empty_cell()
                    cell = self.board.get_cell(player_choice)
                    if cell.status != "X":
                        raise Exception("The cell does not belong to you")
                    if self.are_adjacent(cell, empty_cell):
                        self.board.update_cell(empty_cell,"X")
                        self.board.update_cell(cell," ")
                        self.board.print_board()
                        if self.check_win("X") == 1:
                            print("YOU HAVE WON")
                            break
                        self.turn = 1
                        print("Moved from ",cell.x,cell.y,"to",empty_cell.x,empty_cell.y)
                    else:
                        print("Cells are not adjacent")
                except Exception as er:
                    print(er)
            else:
                #Computer turn
                found_move = False
                empty_cell = self.board.get_empty_cell()
                while found_move == False:
                    move_x = randint(1,3)
                    move_y = randint(1,3)
                    move = move_x*10+move_y
                    cell = self.board.get_cell(str(move))
                    if cell.status == "O" and self.are_adjacent(cell, empty_cell):
                        found_move = True
                        self.board.update_cell(cell," ")
                        self.board.update_cell(empty_cell, "O")
                        self.print_board()
                        print("Computer has moved", move_x,move_y, "to",empty_cell.x,empty_cell.y)
                        self.turn = 0
                if self.check_win("O") == 1:
                    print("Computer has WON")
                    break
 
       
    def are_adjacent(self,cell,cell2):
        posibx = [-1,-1,-1,0,1,1,1,0]
        posiby = [-1,0,1,1,1,0,-1,-1]
        for i in range(0,8):
            if cell.x - posibx[i] == cell2.x and cell.y - posiby[i] == cell2.y:
                return 1
        return 0
                    
    def check_win(self,who):
        win = self.check_rows(who)
        if win == 1:
            return 1
        win = self.check_columns(who)
        if win == 1:
            return 1
        win = self.check_diagonals(who)
        if win == 1:
            return 1
        return 0
        
    def check_rows(self,who):
        for i in range(1,4):
            count = 0
            for j in range(1,4):
                if self.board.get_status(i,j) == who:
                    count = count+1
            if count == 3:
                return 1
        return 0
    
           
    def can_player_win(self):
        #check rows
        for i in range(1,4):
            count = 0
            n = False
            for j in range(1,4):
                if self.board.get_status(i,j) == "O":
                    n = True
                if self.board.get_status(i,j) == "X":
                    count = count+1
                elif self.board.get_status(i,j) == " ":
                    empty_one = self.board.get_cell2(i,j)
            if count == 2 and n == False:
                return empty_one
        #check columns
        for i in range(1,4):
            count = 0
            n=False
            for j in range(1,4):
                if self.board.get_status(j,i) == "O":
                    n=True
                if self.board.get_status(j,i) == "X":
                    count = count+1
                elif self.board.get_status(j,i) == " ":
                    empty_one = self.board.get_cell2(j,i)
            if count == 2 and n==False:
                return empty_one
        #check diags
        count = 0
        n=False
        for i in range(1,4):
            if self.board.get_status(i,i) == "O":
                    n=True
            if self.board.get_status(i,i) == "X":
                count = count+1
            elif self.board.get_status(i,i) == " ":
                empty_one = self.board.get_cell2(i,i)
        if count == 2 and n==False:
            return empty_one
        #diag2
        count = 0
        n=False
        for i in range(1,4):
            if self.board.get_status(i,4-i) == "O":
                    n=True
            if self.board.get_status(i,4-i) == "X":
                count = count+1
            elif self.board.get_status(i,4-i) == " ":
                empty_one = self.board.get_cell2(i,4-i)
        if count == 2 and n==False:
            return empty_one
        return 0
    
    def check_columns(self,who):
        for i in range(1,4):
            count = 0
            for j in range(1,4):
                if self.board.get_status(j,i) == who:
                    count = count+1
            if count == 3:
                return 1
        return 0
    
    def check_diagonals(self,who):
        if self.board.get_status(1,1) == who and self.board.get_status(3,3) == who and self.board.get_status(2,2) == who:
            return 1
        if self.board.get_status(3,1) == who and self.board.get_status(2,2) == who and self.board.get_status(1,3) == who:
            return 1
        return 0