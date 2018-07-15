#!/usr/bin/python3
"""
classes:
ChessBoard

variables:
whiteTurn
board
bk, wk
pickedPiece

functions:
print()
touchSquare()
"""
from pieces import *

class Chess:

    rowDict = { "1":0, "2":1, "3":2, "4":3, "5":4, "6":5, "7":6, "8":7 }
    columnDict = { "A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7 }

    
    def __init__(self):
        self.whiteTurn = True
        self.board = [[None for x in range(8)] for y in range(8)]
        self.bk = King(False, 0, 4)
        self.wk = King(True, 7, 4)
        self.pickedPiece = None
        self.__addPieces()


    def __addPieces(self):
        for j in range(8):
            self.board[6][j] = Pawn(True, 6, j)
            self.board[1][j] = Pawn(False, 1, j)

        self.board[0][4] = self.bk
        self.board[7][4] = self.wk
        self.board[0][3] = Queen(False, 0, 3)
        self.board[7][3] = Queen(True, 7, 3)
        self.board[7][1] = Knight(True, 7, 1)
        self.board[0][1] = Knight(False, 0, 1)
        self.board[7][6] = Knight(True, 7, 6)
        self.board[0][6] = Knight(False, 0, 6)
        self.board[7][2] = Bishop(True, 7, 2)
        self.board[0][2] = Bishop(False, 0, 2)
        self.board[7][5] = Bishop(True, 7, 5)
        self.board[0][5] = Bishop(False, 0, 5)
        self.board[7][0] = Rook(True, 7, 0)
        self.board[0][0] = Rook(False, 0, 0)
        self.board[7][7] = Rook(True, 7, 7)
        self.board[0][7] = Rook(False, 0, 7)


    def debug(self):
        print('')
        print('')
        print(self.pickedPiece)
        print('white' if self.whiteTurn else 'black')


    def print(self):
        pBoard = [[0 for x in range(8)] for y in range(8)]
        self.debug()        
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == None:
                    pBoard[i][j] = '  '
                else:
                    pBoard[i][j] = self.board[i][j].color + \
                                   self.board[i][j].name
        for j in range(8):
            print(j, end=' ')
            print(pBoard[j])
        for j in range(8):
            print('    ', j, end='')

        print('')


    def __wrongTurn(self, row, col):
        if self.board[row][col].isWhite != self.whiteTurn:
            print('wrong turn')
            return True
        else:
            return


    def __pickPiece(self, row, col):
        if self.board[row][col] and not self.__wrongTurn(row, col):
            self.pickedPiece = (row, col)
            return True
        else:
            print('no piece there / wrong turn')
            return False
        

    def __movePiece(self, row, col):
        oldrow = self.pickedPiece[0]
        oldcol = self.pickedPiece[1]
        if self.board[oldrow][oldcol].moveIsValid(row, col, self.board):
            temp = self.board[row][col]
            # self.board[row][col] = self.board[oldrow][oldcol]
            # self.board[oldrow][oldcol] = None
            self.whiteTurn ^= True
            self.board[oldrow][oldcol].move(row, col, self.board)
            if self.__checkMate():
              # self.board[oldrow][oldcol] = self.board[row][col]
              # self.board[row][col] = temp
              self.whiteTurn ^= True
              self.board[row][col].move(oldrow, oldcol, self.board)
              self.board[row][col] = temp
              print('king under threat')
            
        else:
            print('invalid move')
        self.pickedPiece = None


    def __checkMate(self):
        if not self.whiteTurn:
            return self.wk.underThreat(self.board)
        else:
            return self.bk.underThreat(self.board)


    # def movePiece(self, row, col, newrow, newcol):
    #     piece = self.board[row][col]
    #     self.board[piece.row][piece.col] = None
    #     piece.row, piece.col = newrow, newcol
    #     self.board[newrow][newcol] = piece

        
    # def __pickPiece(self, row, col):
    #   if self.board[row][col] and \
    #      self.board[row][col].isWhite == self.whiteTurn:
    #       self.pickedPiece = self.board[row][col]
    #   else:
    #       print('no piece there / wrong turn')        
        

    # def wrongTurn(self, row, col):
    #   if self.board[row][col].isWhite != self.whiteTurn:
    #       print('wrong turn')
    #       return True


    # def makeMove(self, row, col):
    #   if self.pickedPiece.moveIsValid(row, col, self.board):
    #       self.movePiece(self.pickedPiece.row, self.pickedPiece.col, row, col)

    #       if (self.whiteTurn and self.wk.underThreat(self.board)) or \
    #          (not self.whiteTurn and self.bk.underThreat(self.board)):
    #           self.movePiece(row, col, self.pickedPiece.row, self.pickedPiece.col)
    #           print('king under threat')
    #       else:
    #           self.whiteTurn ^= True                
    #   else:
    #       print('invalid move')
    #   self.pickedPiece = None


    def touchSquare(self, row, col):
        if self.pickedPiece:
            self.__movePiece(row, col)
            return False
        else:
            return self.__pickPiece(row, col)


def playchess():
    chess = Chess()
    
    while(True):
        chess.print()
        row = int(input('row: '))
        col = int(input('col: '))
        chess.touchSquare(row, col)


if __name__ == "__main__":
    playchess()


