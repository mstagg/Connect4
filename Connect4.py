#Connect Four
#Matthew Stagg
#6/18/2014

import Board
import AI

Connect4 = Board.Board()

#Main Game Play Loop		
while(True):
#Player 1 turn
	Connect4.PrintBoard()
	column = int(raw_input()) - 1
	Connect4.Move(1, column)
	if Connect4.CheckWin(1) == True:
		Connect4.PrintBoard()
		print('Player 1 Wins!')
		raw_input('Press Enter...')
		break

#Player 2 turn
	#Connect4.PrintBoard()
	AI.Turn(Connect4)
	if Connect4.CheckWin(2) == True:
		Connect4.PrintBoard()
		print('Player 2 Wins!')
		raw_input('Press Enter...')
		break