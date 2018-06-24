#!/usr/bin/python3
from chess import *
from tkinter import *

squarecoords = {}

images = {}

def openimages():
	piecenames = ['bR', 'bN', 'bB', 'bQ', 'bK', 'bP', 'wR', 'wN', 'wB', 'wQ', 'wK', 'wP']
	directory = "../graphics/"
	filetype = ".gif"
	for name in piecenames:
		path = directory + name + filetype
		images[name] = PhotoImage(file=path)



def callback(event, gui):
	
	coords = squarecoords[event.widget]
	
	gui.chess.touchSquare(coords[0], coords[1])
	print(squarecoords[event.widget])
	gui.draw()
	if gui.chess.whiteTurn:
		gui.root.title('white')
	else:
		gui.root.title('black')

	# board.print()
def getcolor(j, k):
	if (j + k) % 2 == 0:
		return '#e5f2ff'
	else:
		return '#97bbd9'



def enter_callback(event, gui):
	# callback for mouseover square
	event.widget.configure(bg='red')	# highlights the square you mouseover

	row = event.widget.grid_info()['row']
	column = event.widget.grid_info()['column']
	if not gui.board[row][column]: return

	for square in gui.squares:
		coords = squarecoords[square]
		j, k = coords[0], coords[1]
		if gui.board[row][column].moveIsValid(j, k, gui.board):
			square.configure(bg='green')

	# for y in range(8):
	# 	for x in range(8):
	# 		if gui.board[row][column] and gui.board[row][column].moveIsValid(y, x, gui.board):
	# 			gui.squares[(y+1) * x].configure(bg='green')	# highlights the squares its possible to move

	# event.widget.itemconfig(bg='red')	
	# print(b.winfo_width(), b.winfo_height())





def exit_callback(event, gui):
	# resets color of squares
	for square in gui.squares:
		coords = squarecoords[square]
		j, k = coords[0], coords[1]
		color = getcolor(j, k)
		square.configure(bg=color)


class ChessGui:
	'ChessGui doc string'
	
	def __init__(self):
		self.root = Tk()
		self.chess = Chess()
		self.board = self.chess.board

		openimages()

		self.squares = []
		for j in range(8):
			for k in range(8):
				color = getcolor(j, k)


				c = Canvas(self.root, bg=color, height=50, width=50)
				c.bind("<Button-1>", lambda event: callback(event, self))
				c.bind("<Enter>", lambda event: enter_callback(event, self))
				c.bind("<Leave>", lambda event: exit_callback(event, self))



				c.grid(row=j,column=k)
				squarecoords[c] = [j, k]



				self.squares.append(c)
				self.squares
		self.draw()

		self.root.mainloop()


	def draw(self):
		for square in self.squares:
			j, k = squarecoords[square][0], squarecoords[square][1]
			square.delete('all')
			if self.board[j][k] != None:
				piecename = self.board[j][k].color + self.board[j][k].name
				im = square.create_image(0, 0, anchor=NW, image=images[piecename])





if __name__ == '__main__':
	print(ChessGui.__name__)
	ChessGui()

