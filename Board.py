class Board:

#Instantiate new board
	def __init__(self):
		print('NewBoard')
		global board
		board = []
		for n in range(7):
			board.append([' '] * 6)
	
#Prints the board in current state
	def PrintBoard(self):
		print('PrintBoard')
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
	
#Select column to drop piece
#If column is full, return False
#Else, return True	
	def Move(self, player, column):
		print('PlayerMove')
		if player == 1:
			piece = 'X'
		elif player == 2:
			piece = 'O'
		if board[column][0] != ' ':
			return False
		row = 6
		while(row >= 0):
			row -= 1
			if board[column][0] == ' ' and board[column][row] == ' ':
				board[column][row] = piece
				return True

#Check if there are four pieces in a row
#If yes, return true
#Else, return false				
	def CheckWin(self, player):
		print('CheckWin')
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