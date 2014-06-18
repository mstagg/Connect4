#For use with Connect Four
#Contains classes and methods that interact directly with the game board

class Board:

#Instantiate new board
	def __init__(self):
		global board
		board = []
		for n in range(7):
			board.append([' '] * 6)
	
#Prints the board in current state
	def PrintBoard(self):
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
	
#Change point on board to a given value
	def Modify(self, x, y, val):
		board[x][y] = val

#Check if point on board is equal to given value
#If point is equal to value, return True
#Else, return False
	def Check(self, x, y, val):
		if board[x][y] == val:
			return True
		else:
			return False

#Check if column is full
#If yes, return True
#Else, return False				
	def ColumnFull(self, column):
		if board[column][0] != ' ':
			return True
		else:
			return False

#Select column to drop piece
#If column is full, return False
#Else, return True	
	def Move(self, player, column):
		if self.ColumnFull(column) == False:
			if player == 1:
				piece = 'X'
			elif player == 2:
				piece = 'O'
			row = 6
			while(row >= 0):
				row -= 1
				if board[column][row] == ' ':
					board[column][row] = piece
					break

#Used by AI to check moves
#Removes the top piece in a given row
	def UndoMove(self, column):
		row = 0
		while(row <= 5):
			if board[column][row] == ' ':
				row += 1
			else:
				board[column][row] = ' '
				break
	
#Used by AI to get top piece in a given row
#Returns the y-value of the top piece in a given row
	def GetTop(self, column):
		row = 0
		while(row <= 5):
			if board[column][row] == ' ':
				row += 1
			else:
				return row
		return row

#Check if entire board is full
#If yes, return True
#Else, return False
	def BoardFull(self):
		if board[0][0] != ' ' and board[1][0] != ' ' and board[2][0] != ' ' and board[3][0] != ' ' and board[4][0] != ' ' and board[5][0] != ' ' and board[6][0] != ' ':
			return True
		else:
			return False

#Check if there are four pieces in a row
#If yes, return true
#Else, return false				
	def CheckWin(self, player):
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
				
				#Diagonal down win condition
				try:
					if board[x][y] == piece and board[x + 1][y + 1] == piece and board[x + 2][y + 2] == piece and board[x + 3][y + 3] == piece:
						return True     
					else:
						pass
				except:
					pass
				
				#Diagonal up win condition
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