#For use with Connect Four
#Contains functions that control computer AI

import Board
import copy

def CanWin(TempGame, column):
	TempGame.Move(2, column)
	if TempGame.CheckWin(2) == True:
		TempGame.UndoMove(column)
		return True
	else:
		TempGame.UndoMove(column)
		return False
		
def CanLose(TempGame, column):
	TempGame.Move(1, column)
	if TempGame.CheckWin(1) == True:
		TempGame.UndoMove(column)
		return True
	else:
		TempGame.UndoMove(column)
		return False


def MinMax(Game):
	TempGame = copy.deepcopy(Game)
	min = 100
	choice = 0
	for x in range(7):
		if TempGame.ColumnFull(x) == True:
			continue
		if x == 3:
			if TempGame.Check(3, 5, ' ') == True:
				heuristic = 0
			else:
				heuristic = 2
		elif x == 2:
			if TempGame.Check(2, 5, ' ') == True:
				heuristic = 1
			else:
				heuristic = 3
		elif x == 4:
			if TempGame.Check(4, 5, ' ') == True:
				heuristic = 1
			else: 
				heuristic = 3
		elif x == 1 or x == 5:
			heuristic = 4
		else:
			heuristic = 5
		if CanWin(TempGame, x) == True:
			heuristic -= 100
		elif CanLose(TempGame, x) == True:
			heuristic -= 50
			
		# if TempGame.CheckDirection(x, TempGame.GetTop, 'n') == True:
			# heuristic += 1
			# if TempGame.CheckDirection(x, TempGame.GetTop - 1, 'n') == True:
				# heuristic += 1
		# elif TempGame.CheckDirection(x, TempGame.GetTop, 's') == True:
			# heuristic += 1
			# if TempGame.CheckDirection(x, TempGame.GetTop + 1, 's') == True:
				# heuristic += 1
		# elif TempGame.CheckDirection(x, TempGame.GetTop, 'e') == True:
			# heuristic += 1
			# if TempGame.CheckDirection(x + 1, TempGame.GetTop, 'e') == True:
				# heuristic += 1
		# elif TempGame.CheckDirection(x, TempGame.GetTop, 'w') == True:
			# heuristic += 1
			# if TempGame.CheckDirection(x - 1, TempGame.GetTop, 'w') == True:
				# heuristic += 1
		# elif TempGame.CheckDirection(x, TempGame.GetTop, 'ne') == True:
			# heuristic += 1
			# if TempGame.CheckDirection(x + 1, TempGame.GetTop - 1, 'ne') == True:
				# heuristic += 1
		# elif TempGame.CheckDirection(x, TempGame.GetTop, 'nw') == True:
			# heuristic += 1
			# if TempGame.CheckDirection(x - 1, TempGame.GetTop - 1, 'nw') == True:
				# heuristic += 1
		# elif TempGame.CheckDirection(x, TempGame.GetTop, 'se') == True:
			# heuristic += 1
			# if TempGame.CheckDirection(x + 1, TempGame.GetTop + 1, 'se') == True:
				# heuristic += 1
		# elif TempGame.CheckDirection(x, TempGame.GetTop, 'sw') == True:
			# heuristic += 1
			# if TempGame.CheckDirection(x - 1, TempGame.GetTop + 1, 'sw') == True:
				# heuristic += 1
		
		if heuristic < min:
			min = heuristic
			choice = x
	return choice
