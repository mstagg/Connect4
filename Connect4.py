#Connect Four
#Matthew Stagg
#5/6/2014

import Board

Connect4 = Board.Board()
while(True):

#Player 1 turn
	Connect4.PrintBoard()
	column = int(raw_input()) - 1
	Connect4.Move(1, column)
	if Connect4.CheckWin(1) == True:
		Connect4.PrintBoard()
		print('Player 1 Wins!')
		break

#Player 2 turn
	Connect4.PrintBoard()
	column = int(raw_input()) - 1
	Connect4.Move(2, column)
	if Connect4.CheckWin(2) == True:
		Connect4.PrintBoard()
		print('Player 2 Wins!')
		break