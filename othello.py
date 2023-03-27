import random
import sys

moves = 4
versus = 0
turn = 1
players = 0
score1 = 2
score2 = 2
row = -1
col = -1
count = 0

def create_board():
    board = [[0 for r in range(8)] for c in range(8)]
    
    return board

def init_board(board):
    board[3][3] = 1
    board[3][4] = 2
    board[4][3] = 2
    board[4][4] = 1
    
def print_board(board):
    print('    0   1   2   3   4   5   6   7')
    print('   -------------------------------')
    for r in range(8):
        print(' ')
        print(r, end=' ')
        for c in range(8):
            print('| %d' % (board[r][c]), end=' ')
        print('|')
    print(' ')
    print('   -------------------------------\n')
    
def human_play(board, color):
    
    global row
    global col
        
    row = int(input('Enter row: '))
    col = int(input('Enter column: '))
    
    if board[row][col] == 0:    
        if row == 7:
            if col != 7:
                while (board[row][col+1] != versus) and (board[row-1][col] != versus):
                    print("Invalid move! Please re-enter the coordinates.")
                    row = int(input('Enter row: '))
                    col = int(input('Enter column: '))
                    
                    if col == 7:
                        if (board[row][col-1] != versus) and (board[row-1][col] != versus):
                            print("Invalid move! Please re-enter the coordinates.")
                            row = int(input('Enter row: '))
                            col = int(input('Enter column: '))
                        
            else:
                if (board[row][col-1] != versus) and (board[row-1][col] != versus):
                    print("Invalid move! Please re-enter the coordinates.")
                    row = int(input('Enter row: '))
                    col = int(input('Enter column: '))
                    
        if col == 7:
            if row != 7:
                while (board[row][col-1] != versus) and (board[row+1][col] != versus):
                    print("Invalid move! Please re-enter the coordinates.")
                    row = int(input('Enter row: '))
                    col = int(input('Enter column: '))
                    
                    if row == 7:
                        if (board[row][col-1] != versus) and (board[row-1][col] != versus):
                            print("Invalid move! Please re-enter the coordinates.")
                            row = int(input('Enter row: '))
                            col = int(input('Enter column: '))
                        
            else:
                if (board[row][col-1] != versus) and (board[row-1][col] != versus):
                    print("Invalid move! Please re-enter the coordinates.")
                    row = int(input('Enter row: '))
                    col = int(input('Enter column: '))
            
        else:
            while (board[row][col+1] != versus) and (board[row][col-1] != versus) and (board[row-1][col] != versus) and (board[row+1][col] != versus):
                print("Invalid move! Please re-enter the coordinates.")
                row = int(input('Enter row: '))
                col = int(input('Enter column: '))
    
    board[row][col] = color
    
    return True
            
def reverse_count(board, color):
    
    global row
    global col
    global count
    global score1
    global score2
    
    posr = row
    posc = col
    
    for c in range(8):
        if c != col:
            if board[row][c] == color:
                posc = c
                break
                    
    if col > posc:
        for c in range(posc+1, col):
            count = count + 1
            
    else:
        for c in range(col+1, posc):
            count = count + 1
            
    for r in range(8):
        if r != row:
            if board[r][col] == color:
                posr = r
                break
            
    if row > posr:
        for r in range(posr+1, row):
            count = count + 1
            
    else:
        for r in range(row+1, posr):
            count = count + 1

    print("Reverses made:", count, "\n")

def add_checker(board, color):
    
    global row
    global col
    
    posr = row
    posc = col
    
    for c in range(8):
        if c != col:
            if board[row][c] == color:
                posc = c
                break
                    
    if col > posc:
        for c in range(posc+1, col):
            board[row][c] = color
            
    else:
        for c in range(col+1, posc):
            board[row][c] = color
            
    for r in range(8):
        if r != row:
            if board[r][col] == color:
                posr = r
                break
            
    if row > posr:
        for r in range(posr+1, row):
            board[r][col] = color
            
    else:
        for r in range(row+1, posr):
            board[r][col] = color
            
def change_color(color):
    
    global versus
    
    if color == 1:
        versus = 1
        color = 2
        
    else:
        color = 1
        versus = 2
        
    return color
            
def print_score():
    print("Player1 has", score1, "points.")
    print("Player2 has", score2, "points.\n")
                                             
print("Play style:")
print("1) Human vs Com")
print("2) Human vs Human")
players = int(input('Enter your choice: '))

mainBoard = create_board()    
init_board(mainBoard)
print_board(mainBoard)

if players == 1:
    color = 1
    versus = 2
    
else:
    color = random.randint(1, 2)
    if color == 1:
        versus = 2
        print("Player1 is using 1 and Player2 is using 2.")
        
    else:
        versus = 1
        print("Player1 is using 2 and Player2 is using 1.")
                                              
while moves < 64:
    
    if turn == 1:
        print("Player1 is playing...\n")
        human_play(mainBoard, color)
        reverse_count(mainBoard, color)
        add_checker(mainBoard, color)
        score1 = score1 + 1
        score1 = score1 + count
        moves = moves + 1
        score2 = moves - score1
        print_board(mainBoard)
        print_score()
        count = 0
        turn = 2
        
    else:
        if players == 2:
            print("Player2 is playing...\n")
            color = change_color(color)
            human_play(mainBoard, color)
            
        """else:
            computer_play()"""
            
        reverse_count(mainBoard, color)
        add_checker(mainBoard, color)
        score2 = score2 + 1
        score2 = score2 + count
        moves = moves + 1
        score1 = moves - score2
        print_board(mainBoard)
        print_score()
        count = 0
        turn = 1
        color = change_color(color)   
        
if moves == 64:
    if score1 > score2:
        if players == 1:
            print("You won!")  
        
        else:
            print("Player1 won!") 
            
    elif score2 > score1:
        if players == 1:
            print("Com won!")
            
        else:
            print("Player2 won!")
            
    else:
        print("It's a draw!")     