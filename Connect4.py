#Connect Four
#Matthew Stagg
#6/18/2014

import Board
import AI
import random

Game = Board.Board()
order = random.randint(0, 1)

def Player1():
	Game.PrintBoard()
	column = int(raw_input()) - 1
	Game.Move(1, column)
	if Game.CheckWin(1) == True:
		return True
	else:
		return False
		
def Player2():
	Game.PrintBoard()
	column = int(raw_input()) - 1
	Game.Move(2, column)
	if Game.CheckWin(2) == True:
		return True
	else:
		return False
		
def PlayerAI():
	Game.Move(2, AI.MinMax(Game))
	if Game.CheckWin(2) == True:
		return True
	else:
		return False
		
#Main Game Play Loop
if order == 0:		
	while(True):
		if Player1() == True:
			print('Player 1 wins!')
			break
		else:
			if PlayerAI() == True:
				print('Player 2 wins!')
				break
else:
	while(True):
		if PlayerAI() == True:
				Game.PrintBoard()
				print('Player 2 wins!')
				raw_input('Press Enter...')
				break
		else:
			if Player1() == True:
				Game.PrintBoard()
				print('Player 1 wins!')
				raw_input('Press Enter...')
				break