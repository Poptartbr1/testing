from tkinter import *
from functools import partial
from ro.ubb.test.grid import Cell,Plane
from random import randint,choice

class GUI(object):

    def __init__(self,master,grid1,grid2):
        self.board_frame = Frame(master)
        self.grid1 = grid1
        self.grid2 = grid2
        self.text_label = Label(self.board_frame,text="Building Phase",font=("Helvetica",16))
        self.text_label.pack(side=TOP)
        self.cheat = Button(self.board_frame,text="Reveal Planes", command=self.reveal_planes)
        self.cheat.pack(side=BOTTOM)
        self.board_frame.pack(side=TOP,fill=X,expand=1,anchor=N)

    game_phase = 1
    planes = 0
    current_cell = None
    rotation = 1
    enemy_planes = 0
    ai_built = 0
    revealed = 0

    ai_moves = []


    def build_player_grid(self):
        frame1 = Frame(self.board_frame)
        frame1.pack()
        separator = Frame(self.board_frame, height=25, bd=1, relief=SUNKEN)
        separator.pack(fill=Y, padx=5, pady=5)
        self.canvas1 = Canvas(frame1,width=600,height=350)
        self.canvas1.pack(side="left",fill="both")
        for i in range(1,9):
            for j in range(1,9):
                self.canvas = Canvas(self.canvas1, width=60, height=35, bd=1, highlightbackground="black",background="white")
                cell = Cell(i,j, "empty",self.canvas)
                self.grid1.add_cell(cell,self.canvas)
                enter_hover_event = partial(self.enter_hover,cell,self.canvas)
                self.canvas.bind('<Enter>',enter_hover_event)
                exit_hover_event = partial(self.exit_hover,cell,self.canvas)
                self.canvas.bind('<Leave>',exit_hover_event)
                self.canvas.grid(row = i, column=j, columnspan=1)

    def build_ai_grid(self):
        frame2 = Frame(self.board_frame)
        frame2.pack()
        self.canvas2 = Canvas(frame2, width=800, height=350)
        self.canvas2.pack(side=RIGHT)
        for i in range(1,9):
            for j in range(1,9):
                self.canvass = Canvas(self.canvas2, width=60, height=35, bd=1, highlightbackground="black", background="white")
                cell = Cell(i,j, "empty",self.canvass)
                self.grid2.add_cell(cell,self.canvass)
                enterr_hover_event = partial(self.attack_hover,cell,self.canvass)
                self.canvass.bind('<Enter>', enterr_hover_event)
                exitt_hover_event = partial(self.exit_attack_hover,cell,self.canvass)
                self.canvass.bind('<Leave>', exitt_hover_event)
                self.canvass.grid(row = i, column=j, columnspan=1)

    def attack_hover(self, cell, canvas, event):
        if self.game_phase == 2:
            if self.revealed == 1:
                if cell.status != "occupied" and cell.attacked == False:
                    self.grid2.set_canvas(cell, "red")
            else:
                if cell.attacked == False:
                    self.grid2.set_canvas(cell, "red")
            click_event = partial(self.attack_event, cell, canvas)
            canvas.bind('<Button-1>', click_event)

    #PLAYNG PART FINALLY
    def attack_event(self, cell, canvas, event):
        if cell.attacked != True:
            self.grid2.set_cell_attacked(cell)
            if cell.status == "occupied":
                #PLAYER HIT
                args = self.grid2.is_cell_head(cell)
                if args[0] == 1:
                    #HEADSHOT
                    plane = args[1]
                    self.grid2.destroy_plane(plane)
                    self.enemy_planes = self.enemy_planes - 1
                    if self.enemy_planes == 0:
                        self.game_phase = 3
                        self.text_label.configure(text = "GAME OVER! YOU WIN")
                        return
                else:
                    #JUST A HIT
                    self.grid2.set_hit(cell)
            else:
                #PLAYER MISSES
                self.grid2.set_miss(cell)
            #AI ATTACk
            move = self.generate_ai_move()
            self.grid1.set_cell_attacked(move)
            if move.status == "occupied":
                #AI HIT
                args = self.grid1.is_cell_head(move)
                if args[0] == 1:
                    #HEADSHOT
                    plane = args[1]
                    self.grid1.destroy_plane(plane)
                    self.planes = self.planes - 1
                    if self.planes == 0:
                        self.game_phase = 3
                        self.text_label.configure(text = "GAME OVER! YOU LOST")
                else:
                    #JUST A HIT
                    self.grid1.set_hit(move)
                    self.ai_moves.append(move)
            else:
                #AI MISSES
                self.grid1.set_miss(move)



    def generate_ai_move(self):
        length = len(self.ai_moves)
        if length == 0:
            #Generate Random Move
            found = 0
            while found == 0:
                move_x = randint(1,8)
                move_y = randint(1,8)
                cell = self.grid1.get_cell(move_x,move_y)
                if cell.attacked == False:
                    found = 1
        else:
            current_cell = self.ai_moves.pop()
            found = 0
            coords = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
            while found == 0:
                if len(coords) != 0:
                    choose = choice(coords)
                move_x = current_cell.x + choose[0]
                move_y = current_cell.y + choose[1]
                if((move_x > 0 and move_x <= 8) and (move_y > 0 and move_y <= 8)):
                    cell = self.grid1.get_cell(move_x,move_y)
                    if cell.attacked == False:
                        found = 1
                        self.ai_moves.append(current_cell)
                    else:
                        if len(coords) == 0:
                            while found == 0:
                                move_x = randint(1, 8)
                                move_y = randint(1, 8)
                                cell = self.grid1.get_cell(move_x, move_y)
                                if cell.attacked == False:
                                    found = 1
                        if choose in coords:
                            coords.remove(choose)
        return cell







    ######################

    def exit_attack_hover(self, cell, canvas, event):
        if self.game_phase == 2:
            if self.revealed == 1:
                if cell.status != "occupied" and cell.attacked == False:
                    self.grid2.set_canvas(cell, "white")
            else:
                if cell.attacked == False:
                    self.grid2.set_canvas(cell, "white")
            canvas.unbind('<Button-1>')

    #HANDLE AI PLANES
    def reveal_planes(self):
        if self.game_phase != 3:
            self.grid2.reveal_planes()
            self.revealed = 1

    def build_ai_planes(self):
        #create 2 random planes
        while self.ai_built == 0:
            try:
                random_cell_x = randint(1,8)
                random_cell_y = randint(1,8)
                cell = self.grid2.get_cell(random_cell_x,random_cell_y)
                random_rotation = randint(1,4)
                coords = self.get_plane_coords(cell,random_rotation)
                ok = self.check_coords(coords)
                if ok == 1:
                    length = len(coords)
                    head = coords[length-1]
                    plane = Plane(coords,head)
                    self.enemy_planes = self.enemy_planes+1
                    self.grid2.add_plane(plane)
                    print(random_rotation)
                    if self.enemy_planes == 2:
                        self.ai_built = 1
            except KeyError:
                continue

    def test_ai(self):
        for plane in self.grid2.planes:
            print(plane.coords)

    def get_plane_coords(self,cell,rotation):
        x = cell.x
        y = cell.y
        if rotation == 1:
            coords = [[x,y],[x,y+1],[x,y+2],[x-1,y+1],[x-2,y],[x-2,y+1],[x-2,y+2],[x-3,y+1]]
        elif rotation == 2:
            coords = [[x,y],[x+1,y],[x+2,y],[x+1,y+1],[x+1,y+2],[x,y+2],[x+2,y+2],[x+1,y+3]]
        elif rotation == 3:
            coords = [[x,y],[x,y+1],[x,y+2],[x+1,y+1],[x+2,y],[x+2,y+1],[x+2,y+2],[x+3,y+1]]
        elif rotation == 4:
            coords = [[x,y],[x+1,y],[x+2,y],[x+1,y-1],[x+1,y-2],[x,y-2],[x+2,y-2],[x+1,y-3]]
        return coords

    def check_coords(self,coords):
        ok = 1
        for set in coords:
            if ((set[0] < 0 and set[0] > 8) and (set[1] < 0 and set[1] > 8)):
                ok = 0
                break
            else:
                cell = self.grid2.get_cell(set[0],set[1])
                status = self.grid2.get_cell_status(cell)
                if status != "empty":
                    ok = 0
                    break
        return ok


    #######################
    def pressed(self,cell,coords,head,canvas,event):
        self.planes = self.planes+1
        plane = Plane(coords,head)
        self.grid1.add_plane(plane)
        for item in coords:
            cell = self.grid1.get_cell(item[0],item[1])
            self.grid1.update_cell(cell,"occupied")
            self.grid1.set_canvas(cell, "blue")
        canvas.unbind('<Button-1>')
        canvas.unbind('<Button-3>')

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
        if self.planes < 2 and self.game_phase < 2:
            self.current_cell = cell
            args = self.create_hover_plane(cell)
            if args[0] == "green":
                coords = args[1]
                last = len(coords)
                head=coords[last-1]
                click_event = partial(self.pressed,cell,coords,head,canvas)
                canvas.bind('<Button-1>', click_event)
                rotate_event = partial(self.rotate,cell,canvas)
                canvas.bind('<Button-3>', rotate_event)
            else:
                canvas.unbind('<Button-1>')
                canvas.unbind('<Button-3>')
        elif self.game_phase == 1:
            canvas.unbind('<Button-1>')
            canvas.unbind('<Button-3>')
            canvas.unbind('<Enter>')
            canvas.unbind('<Leave>')
            self.text_label.configure(text="Fighting Phase")
            self.game_phase = 2

    def exit_hover(self,cell,canvas,event):
        if self.planes <2 and self.game_phase < 2:
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
