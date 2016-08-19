## minesweeper(n) takes one argument, for how many mines you wish to plant.
## grid is a fixed 29 x 26 size

import itertools
import math
import string

refrow = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
    }

def genboard(level):
    if level == 1:
        w = 8
        h = 8
    elif level == 2:
        w = 16
        h = 16
    else:
        w = 16
        h = 30
        
    board = []
    for c in range(w+1):
        rn = []
        for r in range(h+1):
            rn.append('- ')
        board.append(rn)
    counter = 0
    for i in range(h+1):
        if i > 0:
            if i == 1:
                board[0][i] = ' ' + str(counter) + ' '
            elif i < 9:
                board[0][i] = str(counter) + ' '
            elif i >= 9:
                board[0][i] = str(counter) + ''
        counter += 1
    import string
    al = string.ascii_lowercase
    for r in range(w+1):
        if r == 0:
            board[r][0] = ' '
        else:
            board[r][0] = al[r-1] + ' '
    last_line = []
    for j in range(h+2):
        if j == 0 or j == h+1:
            last_line.append(' ')
        else:
            if j == 1:
                last_line.append(' ' + str(j) + ' ')
            elif j < 9:
                last_line.append(str(j) + ' ')
            elif j >= 9:
                last_line.append(str(j) + '')
    board.append(last_line)
    for k in board:
        if board.index(k) == 0:
            k.append(' ')
        elif board.index(k) == h+1:
            k.append(' ')
        else:
            k.append(al[board.index(k)-1])
    return board

def print_board(board):
    for i in board:
        print '  '.join(i)
    
def mineplacer(n, w, h):
    from random import randint
    counter = 0
    mines = []
    for i in range(n):
        checker = True
        while checker == True:
            (row, col) = randint(1,h), randint(1,w)
            if (row, col) not in mines:
                mines.append((row,col))
                checker = False
    lst = []
    for j in mines:
        for i in range(-1,2):
            lst.append((j[0]-1,j[1] + i))
            lst.append((j[0], j[1] + i))
            lst.append((j[0]+1, j[1] + i))
    return mines

def plus(mines):
    
    lst = []
    for j in mines:
        for i in range(-1,2):
            lst.append((j[0]-1,j[1] + i))
            lst.append((j[0], j[1] + i))
            lst.append((j[0]+1, j[1] + i))
    filt = []
    for i in itertools.ifilterfalse(filt.__contains__, lst):
        filt.append(i)
    return filt

def isVisible(rc, mines):
    vis = False
    if rc not in mines:
        vis = True
    return vis
            
def minechecker(rc, mines, minesplus,board,d):
    dic = {}
    if board[rc[0]][rc[1]] == '- ':
        if rc not in d:
            if isVisible(rc, mines):
                counter = 0
                for i in range(-1,2):
                    if (rc[0]-1, rc[1] + i) in mines:
                        counter += 1
                    if (rc[0], rc[1] + i) in mines:
                        counter += 1
                    if (rc[0]+1, rc[1] + i) in mines:
                        counter += 1
                                
                dic[rc] = counter
    d.update(dic)
    if len(dic) >0 and dic[rc] == 0:
        for i in range(-1,2):
            if (rc[0]-1, rc[1] + i) not in dic:
                minechecker((rc[0]-1, rc[1] + i), mines,minesplus,board,d)
            if (rc[0], rc[1] + i) not in dic:
                minechecker((rc[0], rc[1] + i), mines,minesplus,board,d)
            if (rc[0]+1, rc[1] + i) not in dic:
                minechecker((rc[0]+1, rc[1] + i), mines,minesplus,board,d)          
                

def boardreveal(board, dic):
    for i in dic:
        board[i[0]][i[1]] = str(dic[i]) + ' '
    return board
                
def minecount(board, n):
    counter = 0
    for i in board:
        for j in i:
            if j == 'F ':
                counter += 1
    return "Number of mines left: " + str(n - counter)

def gamechecker(board,num):
    win = False
    counter = 0
    for i in board:
        for j in i:
            if j == 'F ':
                counter += 1
                if counter > num:
                    return False
            elif j == '- ':
                counter += 1
                if counter > num:
                    return False
    if counter == num:
        win = True
    return win,counter
            


def minesweeper(level):
    al = string.ascii_lowercase    
    board = genboard(level)



    if level == 1:
        w = 8
        h = 8
        n = 10
    elif level == 2:
        w = 16
        h = 16
        n = 40
    elif level == 3:
        w = 30
        h = 16
        n = 99
    numOfmines = n  
    mines = mineplacer(n, w, h)
    turn = 1
    minesplus = plus(mines)
    print_board(board)

    while turn >0:
        
        #state 0: check for  valid preliminary input
        #state 1: Guess cell, check for valid cell input
        #state 2: Flag cell, check for valid cell input
        
        state = 0

        #Check for win condition
        if gamechecker(board, numOfmines):
            return "You found all the mines! You win!"

        #Display board        
        print minecount(board, numOfmines) 
        g = raw_input("Pick a tile(Type h for help): ")

        #Determine input
        if g == 'q':
            return "Thank you for playing :)"

        elif g[0] == 'h':                
                g = raw_input("Pick a tile(Type ff to flag, gg to guess, or q to quit): ")
                
        elif g == 'gg':
            
            g = raw_input("Pick a tile(Type xx to guess, or q to quit): ")
            state = 1
            
        elif g == 'ff':
            
            g = raw_input("Pick a tile(Type xx to flag, or q to quit): ")
            state = 2
        elif state != 0:
            break
        else:
            print 'Invalid value!'
            print

        # State 1: Guess cell
        if state == 1:
            try:
                x = int(g[1:])
                if g[0].islower() == True and ord(g[0]) - 97 < h:
                    state = 1

                    rc = (refrow[g[0]], int(g[1:]))
                    d = {} 
                    if (rc[1] > w or rc[1] < 1):
                        print "Oops, invalid value!"
                        print rc[1], w
                    elif board[rc[0]][rc[1]] != '- ':
                        if board[rc[0]][rc[1]] == 'F ':
                            print "That tile is currently flagged!"
                            print
                        else:
                            print "That tile is already visible!"
                            print
                    elif rc in mines:
                        board[rc[0]][rc[1]] = 'm '
                        print_board(board)
                        print "BOOM! You stepped on a mine!"
                        print "Game Over"
                        break
                    else:
                        
                        minechecker(rc, mines, minesplus, board,d)
                                                                                
                        board = boardreveal(board, d)
                        
                        print_board(board)
                        print
                        
                else:
                    print "Invalid value!"
                    
            except ValueError:
                print 'Invalid value!'
                

                
            

        elif state == 2:
            try:
                
                x = int(g[1:])
                if g[0].islower() == True and ord(g[0]) - 97 < h:
                    state = 2
                    rc = (refrow[g[0]], int(g[1:]))
                    if board[rc[0]][rc[1]] == '- ': 
                        board[rc[0]][rc[1]] = 'F '
                        print_board(board)
                        print
                    elif board[rc[0]][rc[1]] == 'F ':
                        board[rc[0]][rc[1]] = '- '
                        print_board(board)
                        print
                    else:
                        print "That tile is already visible!"
                        print
                else:
                    print "Invalid value!"
                    print
            except ValueError:
                print 'Invalid value!'
                print
            



minesweeper(1)                      
                

                    
                    
                    

    
    
