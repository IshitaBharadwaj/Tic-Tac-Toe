# Importing required modules and tools 
import random 
from tkinter import *
from functools import partial 
from tkinter import messagebox 
from copy import deepcopy 
import tkinter.font as tkFont
  
#To decide the turn of which player 
sign = 0
  
# Creating an empty board 
board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] 
board4 = [[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' ']]
  
# Checking if(O/X) won the match or not according to the rules of the game for 3 x 3
def winner(b, l):
    if (b[0][0] == l and b[0][1] == l and b[0][2] == l):
        return True
    elif (b[1][0] == l and b[1][1] == l and b[1][2] == l):
        return True
    elif (b[2][0] == l and b[2][1] == l and b[2][2] == l):
        return True
    elif (b[0][0] == l and b[1][0] == l and b[2][0] == l):
        return True
    elif (b[0][1] == l and b[1][1] == l and b[2][1] == l):
        return True
    elif (b[0][2] == l and b[1][2] == l and b[2][2] == l):
        return True
    elif (b[0][0] == l and b[1][1] == l and b[2][2] == l):
        return True
    elif (b[0][2] == l and b[1][1] == l and b[2][0] == l):
        return True        

# Checking if(O/X) won the match or not according to the rules of the game for 4 x 4
def winner4(b, l):
    if (b[0][0] == l and b[0][1] == l and b[0][2] == l and b[0][3] == l):
        return True
    elif (b[1][0] == l and b[1][1] == l and b[1][2] == l and b[1][3] == l):
        return True
    elif (b[2][0] == l and b[2][1] == l and b[2][2] == l and b[2][3] == l):
        return True
    elif (b[0][0] == l and b[1][0] == l and b[2][0] == l and b[3][0] == l):
        return True
    elif (b[0][1] == l and b[1][1] == l and b[2][1] == l and b[3][1] == l):
        return True
    elif (b[0][2] == l and b[1][2] == l and b[2][2] == l and b[3][2] == l):
        return True
    elif (b[0][3] == l and b[1][3] == l and b[2][3] == l and b[3][3] == l):
        return True
    elif (b[3][0] == l and b[3][1] == l and b[3][2] == l and b[3][3] == l):
        return True
    elif (b[0][0] == l and b[1][1] == l and b[2][2] == l and b[3][3] == l):
        return True
    elif (b[0][3] == l and b[1][2] == l and b[2][1] == l and b[3][0] == l):
        return True        
             
  
# Marking on the button in multi player mode for 3x3: 
def get_text3(i, j, gb, l1, l2): 
    global sign
    global board
    if board[i][j] == ' ': 
        if sign % 2 == 0: 
            l1.config(state=DISABLED) 
            l2.config(state=ACTIVE) 
            board[i][j] = "X"
        else: 
            l2.config(state=DISABLED) 
            l1.config(state=ACTIVE) 
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j]) 
    if winner(board, "X"): 
        gb.destroy() 
        box = messagebox.askyesno("Winner", "Congragulations!!\nPlayer 1 won the match\n Play again?")
        if box:
            sign = 0
            board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] 
            play()
    elif winner(board, "O"): 
        gb.destroy() 
        box = messagebox.askyesno("Winner", "Congragulations!!\nPlayer 2 won the match\n Play again?")
        if box:
            sign = 0
            board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] 
            play()
    elif(isfull()): 
        gb.destroy() 
        box = messagebox.askyesno("Tie Game", "Its a Tie!!\n Play again?") 
        if box:
            sign = 0
            board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] 
            play()

# Marking on the button in multi player mode for 4x4: 
def get_text4(i, j, gb, l1, l2): 
    global sign
    global board4
    if board4[i][j] == ' ': 
        if sign % 2 == 0: 
            l1.config(state=DISABLED) 
            l2.config(state=ACTIVE) 
            board4[i][j] = "X"
        else: 
            l2.config(state=DISABLED) 
            l1.config(state=ACTIVE) 
            board4[i][j] = "O"
        sign += 1
        button[i][j].config(text=board4[i][j]) 
    if winner4(board4, "X"): 
        gb.destroy() 
        box = messagebox.askyesno("Winner", "Congragulations!!\nPlayer 1 won the match\n Play again?")
        if box:
            sign = 0
            board4 = [[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' ']]
            play()
    elif winner4(board4, "O"): 
        gb.destroy() 
        box = messagebox.askyesno("Winner", "Congragulations!!\nPlayer 2 won the match\n Play again?")
        if box:
            sign = 0
            board4 = [[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' ']]
            play()
    elif(isfull4()): 
        gb.destroy() 
        box = messagebox.askyesno("Tie Game", "Its a Tie!!\n Play again?") 
        if box:
            sign = 0
            board4 = [[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' '],[' ',' ',' ',' ']]
            play()
            
# Check if the button can be pressed or not in 3x3 
def isfree(i, j): 
    return board[i][j] == " "

# Check if the button can be pressed or not in 3x3 
def isfree4(i, j): 
    return board4[i][j] == " "
  
# Check the board is full or not in 3 x 3 
def isfull(): 
    flag = True
    for i in board: 
        if(i.count(' ') > 0): 
            flag = False
    return flag 

# Check the board is full or not in 3 x 3 
def isfull4(): 
    flag = True
    for i in board4: 
        if(i.count(' ') > 0): 
            flag = False
    return flag 
  
# GUI of game board for multi player mode for 3x3: 
def gameboard_pl3(game_board, l1, l2): 
    global button 
    button = [] 
    for i in range(3): 
        m = 3+i 
        button.append(i) 
        button[i] = [] 
        for j in range(3): 
            n = j 
            button[i].append(j) 
            get_t3 = partial(get_text3, i, j, game_board, l1, l2) 
            button[i][j] = Button( 
                game_board, bd=5, command=get_t3, height=4, width=8) 
            button[i][j].grid(row=m, column=n) 
    game_board.mainloop() 

# GUI of game board for multi player mode for 3x3: 
def gameboard_pl4(game_board, l1, l2): 
    global button 
    button = [] 
    for i in range(4): 
        m = 4+i 
        button.append(i) 
        button[i] = [] 
        for j in range(4): 
            n = j 
            button[i].append(j) 
            get_t4 = partial(get_text4, i, j, game_board, l1, l2) 
            button[i][j] = Button( 
                game_board, bd=5, command=get_t4, height=4, width=8) 
            button[i][j].grid(row=m, column=n) 
    game_board.mainloop() 

  
# System's next move 
def pc(): 
    possiblemove = [] 
    for i in range(len(board)): 
        for j in range(len(board[i])): 
            if board[i][j] == ' ': 
                possiblemove.append([i, j]) 
    move = [] 
    if possiblemove == []: 
        return
    else: 
        for let in ['O', 'X']: 
            for i in possiblemove: 
                boardcopy = deepcopy(board) 
                boardcopy[i[0]][i[1]] = let 
                if winner(boardcopy, let): 
                    return i 
        corner = [] 
        for i in possiblemove: 
            if i in [[0, 0], [0, 2], [2, 0], [2, 2]]: 
                corner.append(i) 
        if len(corner) > 0: 
            move = random.randint(0, len(corner)-1) 
            return corner[move] 
        edge = [] 
        for i in possiblemove: 
            if i in [[0, 1], [1, 0], [1, 2], [2, 1]]: 
                edge.append(i) 
        if len(edge) > 0: 
            move = random.randint(0, len(edge)-1) 
            return edge[move] 
  
# Marking on the button in single player mode:  
def get_text_pc(i, j, gb, l1, l2): 
    global sign
    global board
    if board[i][j] == ' ': 
        if sign % 2 == 0: 
            l1.config(state=DISABLED) 
            l2.config(state=ACTIVE) 
            board[i][j] = "X"
        else: 
            button[i][j].config(state=ACTIVE) 
            l2.config(state=DISABLED) 
            l1.config(state=ACTIVE) 
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j]) 
    x = True
    if winner(board, "X"): 
        gb.destroy() 
        x = False
        box = messagebox.askyesno("Winner", "Conragulations!!\n You won the match\n Play again?")
        if box:
            sign = 0
            board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] 
            play()
    elif winner(board, "O"): 
        gb.destroy() 
        x = False
        box = messagebox.askyesno("Winner", "Oops!!\nComputer won the match\n Play again?")
        if box:
            sign = 0
            board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] 
            play()
    elif(isfull()): 
        gb.destroy() 
        x = False
        box = messagebox.askyesno("Tie Game", "Its a Tie!!\n Play again? ")
        if box:
            sign = 0
            board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] 
            play()
    if(x): 
        if sign % 2 != 0: 
            move = pc() 
            button[move[0]][move[1]].config(state=DISABLED) 
            get_text_pc(move[0], move[1], gb, l1, l2) 
  
# GUI of game board in single player mode: 
def gameboard_pc(game_board, l1, l2): 
    global button 
    button = [] 
    for i in range(3): 
        m = 3+i 
        button.append(i) 
        button[i] = [] 
        for j in range(3): 
            n = j 
            button[i].append(j) 
            get_t = partial(get_text_pc, i, j, game_board, l1, l2) 
            button[i][j] = Button( 
                game_board, bd=5, command=get_t, height=4, width=8) 
            button[i][j].grid(row=m, column=n) 
    game_board.mainloop() 
  
# Initialize the game board to play with system 
def withpc(game_board): 
    game_board.destroy() 
    game_board = Tk() 
    game_board.title("Tic Tac Toe") 
    l1 = Button(game_board, text="Player : X", width=10) 
    l1.grid(row=1, column=1) 
    l2 = Button(game_board, text = "Computer : O", 
                width = 10, state = DISABLED) 
      
    l2.grid(row = 2, column = 1) 
    gameboard_pc(game_board, l1, l2) 

#Asks user to choose between 3X3 and 4X4 game
def choice(game_board):
    game_board.destroy() 
    
    game_board = Tk()
    game_board.title("3X3 or 4X4")
    wpl3 = partial(withplayer3, game_board)
    wpl4 = partial(withplayer4, game_board)

    three = Button(game_board, text = "3 X 3", command = wpl3,  
                activeforeground = 'light green', 
                  activebackground = "black", bg = "light green",  
                  fg = "black", font = 'summer', bd = 5, pady=2)
    four = Button(game_board, text = "4 X 4", command = wpl4,  
                activeforeground = 'light green', 
                  activebackground = "black", bg = "light green",  
                  fg = "black", font = 'summer', bd = 5, pady=2)
    three.pack()
    four.pack()
    game_board.mainloop()
   
# Initialize the game board to play with another player for 3x3
def withplayer3(game_board):
  
    game_board.destroy() 
    game_board = Tk() 
    game_board.title("Tic Tac Toe") 
    l1 = Button(game_board, text = "Player 1 : X", width = 10) 
      
    l1.grid(row = 1, column = 1) 
    l2 = Button(game_board, text = "Player 2 : O",  
                width = 10, state = DISABLED) 
      
    l2.grid(row = 2, column = 1) 
    gameboard_pl3(game_board, l1, l2) 

# Initialize the game board to play with another player for 4x4
def withplayer4(game_board):
  
    game_board.destroy() 
    game_board = Tk() 
    game_board.title("Tic Tac Toe") 
    l1 = Button(game_board, text = "Player 1 : X", width = 10) 
      
    l1.grid(row = 1, column = 1, columnspan=2) 
    l2 = Button(game_board, text = "Player 2 : O",  
                width = 10, state = DISABLED) 
      
    l2.grid(row = 2, column = 1,columnspan=2) 
    gameboard_pl4(game_board, l1, l2) 

# main function 
def play():
    global menu
    menu = Tk() 
    
    menu.title("Tic Tac Toe") 
    wpc = partial(withpc, menu) 
   
    c = partial(choice,menu)
    def dest():
        menu.destroy()
      
    head = Button(menu, text = "  Welcome to tic-tac-toe game  ", 
                  activeforeground = 'black', 
                  activebackground ="orange", bg = "black",  
                  fg = "orange", font = 'summer', bd = 5,pady=12) 
      
    B1 = Button(menu, text = "Single Player", command = wpc,  
                activeforeground = 'dark blue', 
                  activebackground = "cyan", bg = "dark blue",  
                  fg = "cyan", font = 'summer', bd = 5, height=5, width=10)
      
    B2 = Button(menu, text = "Multi Player", command = c ,activeforeground = 'light green', 
                  activebackground = "black", bg = "light green",  
                  fg = "black", font = 'summer', bd = 5)
      
    B3 = Button(menu, text = "Exit", command =dest, activeforeground = 'red', 
                activebackground = "yellow", bg = "red", fg = "yellow", 
                font = 'summer', bd = 5,) 
    head.grid(row=1,column=0,columnspan=7,pady=6) 
    B1.grid(row=2,column=0,pady=6,padx=1.5)
    #B1.size(height=100, width=100)
    B2.grid(row=2,column=6,pady=6,padx=1.5) 
    B3.grid(row=5,column=3, columnspan=3,pady=6) 
    menu.mainloop() 
  
# Starting the game  
play()
