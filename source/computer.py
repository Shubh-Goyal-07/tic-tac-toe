import numpy as np

def checkRow(board, i, j):
    x=0
    o=0
    for k in range(3):
        if board[i][k]=='X':
            x+=1
        elif board[i][k]=='O':
            o+=1
    if x==2:
        return 2
    elif o==2:
        return 1
    elif x==1 and o==0:
        return 0
    elif o==1 and x==1:
        return -1
    elif o==1 and x==0:
        return -1
    elif x==0 and o==0:
        return 0

def checkCol(board, i, j):
    x=0
    o=0
    for k in range(3):
        if board[k][j]=='X':
            x+=1
        elif board[k][j]=='O':
            o+=1
    if x==2:
        return 2
    elif o==2:
        return 1
    elif x==1 and o==0:
        return 0
    elif o==1 and x==1:
        return -1
    elif o==1 and x==0:
        return -1
    elif x==0 and o==0:
        return 0

def checkDiag1(board, i, j):
    x=0
    o=0
    if abs(i-j)==0 and i!=1:
        for k in range(3):
            if board[k][k]=='X':
                x+=1
            elif board[k][k]=='O':
                o+=1
    if x==2:
        return 2
    elif o==2:
        return 1
    elif x==1 and o==0:
        return 0
    elif o==1 and x==1:
        return -1
    elif o==1 and x==0:
        return -1
    elif x==0 and o==0:
        return 0
    return 0

def checkDiag2(board, i, j):
    x=0
    o=0
    if (abs(i-j)==0 and i==1) or abs(i-j)==2:
        for k in range(3):
            if board[k][2-k]=='X':
                x+=1
            elif board[k][2-k]=='O':
                o+=1
    if x==2:
        return 2
    elif o==2:
        return 1
    elif x==1 and o==0:
        return 0
    elif o==1 and x==1:
        return -1
    elif o==1 and x==0:
        return -1
    elif x==0 and o==0:
        return 0
    return 0

def checkWinner(board):
    winner = None

    for i in range(3):
        if board[i,0] == board[i,1] == board[i,2]:
            winner = board[i,0]

        elif board[0,i] == board[1,i] == board[2,i]:
            winner = board[0,i]

    if board[0,0] == board[1,1] == board[2,2]:
        winner = board[0,0]

    if board[0,2] == board[2,0] == board[1,1]:
        winner = board[0,2]

    if winner == None and not isEmpty(board):
        winner = 'Draw'
    
    return winner

def playWithComputer(board):
    score=-100
    for i in range(3):
        for j in range(3):
            if board[i, j]=='':
                x = max(checkCol(board, i, j), checkRow(board, i, j), checkDiag1(board, i, j), checkDiag2(board, i, j))
                if x>score:
                    score = x
                    a = (i,j)

    # board[a[0], a[1]] = 'X'
    # return board

    return a

def isEmpty(board):
    flag=0
    for i in range(3):
        for j in range(3):
            if board[i][j]=='':
                flag=1
                break

    if flag:
        return True
    else:
        return False

board = np.array([['', '', ''], ['', '', ''], ['', '', '']])

# while isEmpty(board):
#     print(board)
#     x,y = map(int, input('Make a move:').split())
#     board[x,y]='O'
#     if not isEmpty(board):
#         print(checkWinner(board))
#         break
#     if checkWinner(board)=='O':
#         print(checkWinner(board))
#         break
#     board = playWithComputer(board)
#     if checkWinner(board)=='X':
#         print(checkWinner(board))
#         break
