#For use with Connect Four
#Contains functions that control computer AI

import Board

#Check if AI can win this turn
#If yes, make winning move and return True
#Else, return False
def CanWin(Connect4):
	for x in range(7):
		if Connect4.ColumnFull(x) == False:
			Connect4.Move(2, x)
			if Connect4.CheckWin(2) == True:
				return True
			else:
				Connect4.UndoMove(x)
	return False

#Check if AI can lose this turn
#If yes, block player from winning and return True
#Else, return False
def CanLose(Connect4):
	for x in range(7):
		if Connect4.ColumnFull(x) == False:
			Connect4.Move(1, x)
			if Connect4.CheckWin(1) == True:
				Connect4.UndoMove(x)
				Connect4.Move(2, x)
				return True
			else:
				Connect4.UndoMove(x)
	return False

#Algorithm for choosing column
def ChooseColumn(Connect4):
	if Connect4.Check(3, 5, ' ') == True:
		Connect4.Modify(3, 5, 'O')
	elif Connect4.Check(2, 5, ' ') == True:
		Connect4.Modify(2, 5, 'O')
	elif Connect4.Check(4, 5, ' ') == True:
		Connect4.Modify(4, 5, 'O')
	elif Connect4.ColumnFull(3) ==  False:
		Connect4.Move(2, 3)
	elif Connect4.ColumnFull(2) ==  False:
		Connect4.Move(2, 2)
	elif Connect4.ColumnFull(4) ==  False:
		Connect4.Move(2, 4)
	elif Connect4.ColumnFull(1) ==  False:
		Connect4.Move(2, 1)
	elif Connect4.ColumnFull(5) ==  False:
		Connect4.Move(2, 5)
	elif Connect4.ColumnFull(0) ==  False:
		Connect4.Move(2, 0)
	elif Connect4.ColumnFull(6) ==  False:
		Connect4.Move(2, 6)

#Entire AI turn in sequence
def Turn(Connect4):
	if CanWin(Connect4) == True:
		return
	elif CanLose(Connect4) == True:
		return
	else:
		ChooseColumn(Connect4)
		return