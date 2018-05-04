

class Board:
	wPieces = ['wR','wN','wB','wQ','wK','wB','wN','wR']
	wPieces += 8 * ['wP']
	bPieces = ['bR','bN','bB','bQ','bK','bB','bN','bR']
	bPieces += 8 * ['bP']

	rows = ['H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']

	board = [[0 for x in range(8)] for y in range(8)]

	def __init__(self):
		self.board[0] = self.bPieces[:8]
		self.board[1] = self.bPieces[8:]
		self.board[6] = self.wPieces[8:]
		self.board[7] = self.wPieces[:8]


	def print(self):
		pBoard = self.board
		for i in range(8):
			for j in range(8):
				if pBoard[i][j] == 0:
					pBoard[i][j] = '  '
		for j in range(8):
			print(self.rows[j], end=' ')
			print(pBoard[j])
		for j in range(8):
			print('    ', j+1, end='')

		print('')



def playchess():
	board = Board()
	board.print()

playchess()


