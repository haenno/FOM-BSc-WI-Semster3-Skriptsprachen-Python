# 6. Vorlesung 30.10.2020, Skript Python 4 (07_Python_04.pdf)
# Übung 2: GUI, Snake light

from tkinter import *
import random

ROWS = 20
COLS = ROWS
PADDING = 1
BOXSIZE = 25

def game_over():
    global SPIELFELD
    for i in range(ROWS):
        for j in range(COLS):
            SPIELFELD[i][j] = 9

def new_target():
    global SPIELFELD
   
    try_target = True
    while try_target: 
        new_target_y = int(random.uniform(0,COLS))
        new_target_x = int(random.uniform(0,ROWS))
        if SPIELFELD[new_target_y][new_target_x] == 0:
            SPIELFELD[new_target_y][new_target_x] = 2
            try_target = False

def set_player(x,y):
    global SPIELFELD
    
    for i in range(ROWS):
        for j in range(COLS):
            if SPIELFELD[i][j] == 3: 
                SPIELFELD[i][j] = 0

    SPIELFELD[x][y] = 3

def add_trail():
    global TRAIL, SPIELFELD
    TRAIL.insert(0,(int(get_player_pos("x")),int(get_player_pos("y"))))

def move_trail():
    global TRAIL, SPIELFELD
    if len(TRAIL)>0:
        delete_trailend_XY = TRAIL.pop()
        SPIELFELD[delete_trailend_XY[0]][delete_trailend_XY[1]] = 0
        TRAIL.insert(0,(get_player_pos("x"), get_player_pos("y")))
      

def movement_logic(new_player_x, new_player_y):
    print("TRAIL move is: %s" % TRAIL)
    if new_player_x < 0 or new_player_x >= ROWS or new_player_y < 0 or new_player_y >= COLS or SPIELFELD[new_player_x][new_player_y] == 1:
        game_over()
    else: 
        if SPIELFELD[new_player_x][new_player_y] == 2:
            add_trail()
            new_target()
        else:
            move_trail()  
        set_player(new_player_x,new_player_y)
            

def get_player_pos(axis):
    for i in range(ROWS):
        for j in range(COLS):
            if SPIELFELD[i][j] == 3:
                if axis == "x":
                    return int(i)
                elif axis == "y":
                    return int(j)

def input_up():
    movement_logic(get_player_pos("x"), get_player_pos("y")-1)
    print_field()

def input_left():
    movement_logic (get_player_pos("x")-1, get_player_pos("y"))
    print_field()

def input_right():
    movement_logic (get_player_pos("x")+1, get_player_pos("y"))
    print_field()

def input_down():
    movement_logic (get_player_pos("x"), get_player_pos("y")+1)
    print_field()

def print_field():
    global SPIELFELD
    cnv.delete("all")
    for i in range(ROWS):
        x = (i*(BOXSIZE+PADDING))+BOXSIZE
        for j in range(COLS):
            y = (j *(PADDING + BOXSIZE))+BOXSIZE
            x2= x + BOXSIZE
            y2= y + BOXSIZE

            #set marker for trail
            if (i,j) in TRAIL and SPIELFELD[i][j] != 3:
                SPIELFELD[i][j] = 1

            if SPIELFELD[i][j] == 0:
                #empty
                color = "black"
            elif SPIELFELD[i][j] == 1:
                #playertrail
                color = "white"
            elif SPIELFELD[i][j] == 2:
                #target
                color = "green"
            elif SPIELFELD[i][j] == 3:
                #player
                color = "yellow"
            elif SPIELFELD[i][j] == 9:
                #gameover
                color = "red"                
            else:
                #fehler
                color = "pink"

            cnv.create_rectangle(x,y,x2,y2,fill=color,outline="")
    print("TRAIL print is: %s" % TRAIL)

def new_field():
    the_new_field =[]
    for i in range(ROWS):
        row = []
        for j in range(COLS):
            row.append(0)
        the_new_field.append(row)
    return the_new_field


gui = Tk()
gui.title("Snake light...")

cnv = Canvas (  gui, 
                width=((ROWS+1)*(BOXSIZE+PADDING))+BOXSIZE-(PADDING*2), 
                height=((COLS+1)*(BOXSIZE+PADDING))+BOXSIZE-(PADDING*2), 
                background="grey")

cnv.pack()

button_up = Button(gui, text="up", width=15, command=input_up)
button_left = Button(gui, text="left", width=15, command=input_left)
button_right = Button(gui, text="right", width=15, command=input_right)
button_down = Button(gui, text="down", width=15, command=input_down)

button_up.pack(side=TOP)
button_left.pack(side=LEFT)
button_right.pack(side=RIGHT)
button_down.pack(side=BOTTOM)


# init and prepare game
TRAIL = list()

SPIELFELD = new_field() # create new playfield
SPIELFELD[int(round(ROWS/2,0))][int(round(COLS/2,0))] = 3 # set players dot in the middle
new_target() # set frist target
print_field() # print first field

# rest is started by the 4 directional buttons
mainloop()
