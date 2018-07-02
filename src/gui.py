#!/usr/bin/python3
from chess import *
from tkinter import *

# Global dictionary with cordinates for each canvas square
squarecoords = {}

# Initialize global dictionary with images for each piece
images = {}
def openimages():
    piecenames = ['bR', 'bN', 'bB', 'bQ', 'bK', 'bP', 'wR', 'wN', 'wB', 'wQ', 'wK', 'wP']
    directory = "../graphics/"
    filetype = ".gif"
    for name in piecenames:
        path = directory + name + filetype
        images[name] = PhotoImage(file=path)


def getcolor(j, k):
    # Returns lighter color for squares with even coords and darker for odd
    if (j + k) % 2 == 0:
        return '#e5f2ff'
    else:
        return '#97bbd9'
        

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
                c.bind("<Button-1>", lambda event: self.callback(event, self))
                c.bind("<Enter>", lambda event: self.enter_callback(event, self))
                c.bind("<Leave>", lambda event: self.exit_callback(event, self))

                c.grid(row=j,column=k)
                squarecoords[c] = [j, k]

                self.squares.append(c)
                self.squares
        self.draw()

        self.root.mainloop()

    def draw(self):
        if self.chess.pickedPiece:
            row, col = self.chess.pickedPiece

        for square in self.squares:
            j, k = squarecoords[square][0], squarecoords[square][1]
            square.delete('all')
            if self.board[j][k] != None:
                piecename = self.board[j][k].color + self.board[j][k].name
                im = square.create_image(0, 0, anchor=NW, image=images[piecename])

            if self.chess.pickedPiece and j == row and k == col:         # highlights the picked piece
                square.configure(bg='blue')

    def callback(self, event, gui):
        # callback for clicking on square
        coords = squarecoords[event.widget]
        
        pieceIsPicked = gui.chess.touchSquare(coords[0], coords[1])
        print(squarecoords[event.widget])
        gui.draw()
        
        if gui.chess.whiteTurn:
            gui.root.title('white')
        else:
            gui.root.title('black')

    def enter_callback(self, event, gui):
        # callback for mouseover square. It highlights the squares you can make possible moves
        event.widget.configure(bg='blue')    # and the square you mouseover

        row = event.widget.grid_info()['row']
        column = event.widget.grid_info()['column']

        
        if not gui.board[row][column] or gui.board[row][column].isWhite != self.chess.whiteTurn: return
        gui.board[row][column].underThreat(gui.board)
        

        for square in gui.squares:
            coords = squarecoords[square]
            j, k = coords[0], coords[1]
            if self.chess.pickedPiece == (j, k): continue
            if gui.board[row][column].moveIsValid(j, k, gui.board):
                square.configure(bg='green')

    def exit_callback(self, event, gui):
        # resets color of squares
        for square in gui.squares:
            coords = squarecoords[square]
            j, k = coords[0], coords[1]
            if self.chess.pickedPiece == (j, k): continue
            color = getcolor(j, k)
            square.configure(bg=color)


if __name__ == '__main__':
    print(ChessGui.__name__)
    ChessGui()