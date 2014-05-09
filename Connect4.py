#Connect Four
#Matthew Stagg
#5/6/2014

board = []
for n in range(7):
    board.append([' '] * 6)

#Prints the board in current state
def PrintBoard():
    x = 0
    y = 0
    for val in board[x]:
        x = 0
        print('|'),
        for val in board:
            print(board[x][y]),
            print('|'),
            x += 1
        print
        y += 1
    print('=============================')
    print('| 1 | 2 | 3 | 4 | 5 | 6 | 7 |\n')

#Player 1 selects column to drop their piece
#If column is full or input is not valid, return False
#Else, return True
def PlayerMove(player):
    if player == 1:
        piece = 'X'
    elif player == 2:
        piece = 'O'
        
    choice = raw_input("Player " + str(player) + " , please choose a column to drop your piece: ")

    #Error handling
    try:
        choice = int(choice) - 1
    except:
        print('That is not a number! Please choose a number from 1 to 7.')
        return False

    if choice > 6  or choice < 0:
        print('That number is too big or too small! Please choose a number from 1 to 7.')
        return False
    else:
        row = 6
        while(row >= 0):
            row -= 1
            if board[choice][0] == ' ' and board[choice][row] == ' ':
                board[choice][row] = piece
                return True
            elif board[choice][0] != ' ':
                print('That row is full!')
                return False

#Check if there are four player pieces in a row
#If yes, return true
#Else, return false
def CheckWin(player):
    if player == 1:
        piece = 'X'
    elif player == 2:
        piece = 'O'
    x = 0
    for xVal in board:
        y = 0
        for yVal in xVal:

            #Horizontal win condition
            try:
                if board[x][y] == piece and board[x + 1][y] == piece and board[x + 2][y] == piece and board[x + 3][y] == piece:
                    return True     
                else:
                    pass
            except:
                pass
            
            #Vertical win condition
            try:
                if board[x][y] == piece and board[x][y + 1] == piece and board[x][y + 2] == piece and board[x][y + 3] == piece:
                    return True     
                else:
                    pass
            except:
                pass
            
            #Diagonal up win condition
            try:
                if board[x][y] == piece and board[x + 1][y + 1] == piece and board[x + 2][y + 2] == piece and board[x + 3][y + 3] == piece:
                    return True     
                else:
                    pass
            except:
                pass
            
            #Diagonal down win condition
            try:
                if board[x][y] == piece and board[x + 1][y - 1] == piece and board[x + 2][y - 2] == piece and board[x + 3][y - 3] == piece:
                    return True     
                else:
                    pass
            except:
                pass
            y += 1
        x += 1
    return False

#Run function PlayerMove and CheckWin
#If CheckWin is true, return false
#Else, return true
def PlayerTurn(player):
    while(PlayerMove(player) == False):
        pass
    if(CheckWin(player) == True):
        print("**** Player " + str(player) + " is the winner! ****")
        return False

    
#Gameplay loop
#Game continues as long as PlayerTurn returns true
while(True):
    PrintBoard()
    if(PlayerTurn(1) == False):
        PrintBoard()
        break
    PrintBoard()
    if(PlayerTurn(2) == False):
        PrintBoard()
        break
    
raw_input("Press any button to end game...")
    
