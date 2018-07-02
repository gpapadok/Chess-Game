"""
INTERFACE
classes:
Piece subclasses

variables:
row, col
isWhite
name
color

functions:
moveIsValid(row, col, board)
underThreat(board)
"""
class Piece:
    
    def __init__(self, isWhite, row, col):
        self.isWhite = isWhite
        self.row, self.col = row, col
        self.color = 'w' if self.isWhite else 'b'

        
    def moveIsValid(self, row, col, board):
        if (row < 0 and row > 7) or (col < 0 and col > 7):
            return False
        if (row == self.row and col == self.col):
            return False
        if (board[row][col] != None and board[row][col].isWhite == self.isWhite):
            return False
        return True


    def move(self, row, col, board):
    	self.row, self.col = row, col


    def underThreat(self, board):
        for row in board:
            for piece in row:
                if piece and piece.isWhite != self.isWhite and \
                   piece.moveIsValid(self.row, self.col, board):
                    print('under threat by ', piece.row, piece.col)
                    return True
        return False


class Pawn(Piece):
    
    name = 'P'
    
    def __init__(self, isWhite, row, col):
    	super(Pawn, self).__init__(isWhite, row, col)
    	self.step = -1 if isWhite else 1
    	self.__firstMove = True

    
    def move(self, row, col, board):
    	super(Pawn, self).move(row, col, board)
    	if row == 0 or row == 7:
            board[row][col] = Queen(self.isWhite, row, col)
    	self.__firstMove = False


    def moveIsValid(self, row, col, board):
        if (not super(Pawn, self).moveIsValid(row, col, board)):
            return False

        if self.__firstMove and row == self.row + 2*self.step and board[row][col] == None \
           and self.col == col and board[self.row + self.step][col] == None:
        	return True

        if self.row + self.step == row:
        	if self.col == col and board[row][col] == None:
        		return True
        	elif abs(self.col - col) == 1 and board[row][col] != None and board[row][col].isWhite != self.isWhite:
        		return True
        	else:
        		return False
        else:
        	return False


        # if abs(self.col - col) > 1:
        #     return False
        # if self.__firstMove:
        #     if abs(self.row - row) > 2:
        #         return False
        # else:
        #     if abs(self.row - row) > 1:
        #         return False
        # # print(self.col, col)
        # if self.col != col:
        #     if board[row][col] == None:
        #         return False
        #     else:
        #         return True
        
        # if board[row][col] != None:
        #     return False
        
        # if self.isWhite:
        #     if row > self.row:
        #         return False
        # else:
        #     if row < self.row:
        #         return False        

        # # self.__firstMove = False
        # return True


class King(Piece):
    
    name = 'K'
    
    def moveIsValid(self, row, col, board):
        if not super(King, self).moveIsValid(row, col, board):
            return False
        
        if (abs(self.row - row) > 1 or abs(self.col - col) > 1):
            return False
        
        return True


    # def isSafe(self, board):
    #     for piece in board:
    #         if not piece:
    #             if piece.isWhite != self.isWhite:
    #                 if piece.moveIsValid(self.row, self.col, board):
    #                     return False
    #     return True

        
    #def byBishop(self, board):
        
        
'''
class Queen(Piece):
    
    name = 'Q'

    def moveIsValid(self, row, col, board):
        if not super(Queen, self).moveIsValid(row, col, board):
            return False

        if abs(self.row - row) != abs(self.col - col) and (row != self.row and col != self.col):
            return False

        return not self.__pathIsBlocked(row, col, board)

    def __pathIsBlocked(self, row, col, board):
        if row == self.row:
            if col > self.col:
                step = 1
            else:
                step = -1
            for j in range(col+1, self.col, step):
                if board[row][j] != 0:
                    return True
            return False

        elif col == self.col:
            if row > self.row:
                step = 1
            else:
                step = -1
            for j in range(row+1, self.row, step):
                if board[j][col] != 0:
                    return True
            return False

        if row > self.row:
            xStep = 1
        else:
            xStep = -1

        if col > self.col:
            yStep = 1
        else:
            yStep = -1

        xTemp, yTemp = self.row + xStep, self.col + yStep
        while(xTemp != row and yTemp != col):
            if (board[xTemp][yTemp] != 0):
                return True
            xTemp, yTemp = xTemp + 1, yTemp + 1
        return False
      
'''


class Queen(Piece):
    
    name = 'Q'
    
    def moveIsValid(self, row, col, board):
        if not super(Queen, self).moveIsValid(row, col, board):
            return False
        
        if (abs(self.row - row) != abs(self.col - col)) and \
           (self.row != row and self.col != col):
            return False
        
        return not self.__pathIsBlocked(row, col, board)

    
    def __pathIsBlocked(self, row, col, board):
        if row == self.row:
            if col > self.col:
                step = 1
            else:
                step = -1
                
            for j in range(self.col+step, col, step):
                if board[row][j] != None:
                    return True
            return False
            
        elif col == self.col:
            if row > self.row:
                step = 1
            else:
                step = -1
                
            for j in range(self.row+step, row, step):
                if board[j][col] != None:
                    return True
            return False
           
        else:
            if row > self.row:
                xStep = 1
            else:
                xStep = -1
                
            if col > self.col:
                yStep = 1
            else:
                yStep = -1
                
            xTemp, yTemp = self.row + xStep, self.col + yStep
            while (xTemp != row and yTemp != col):
                if (board[xTemp][yTemp] != None):
                    return True
                xTemp, yTemp = xTemp + xStep, yTemp + yStep
            
            return False
       
        
class Knight(Piece):
    
    name = 'N'
    
    def moveIsValid(self, row, col, board):
        if not super(Knight, self).moveIsValid(row, col, board):
            return False
        
        xDif, yDif = abs(self.row - row), abs(self.col - col)
        
        return (xDif == 2 and yDif == 1) or (xDif == 1 and yDif == 2)
        
    
class Bishop(Piece):
    
    name = 'B'
    
    def moveIsValid(self, row, col, board):
        if not super(Bishop, self).moveIsValid(row, col, board):
            return False
        
        if abs(self.row - row) != abs(self.col - col):
            return False
        
        return not self.__pathIsBlocked(row, col, board)
        
    
    def __pathIsBlocked(self, row, col, board):

        if row > self.row:
            xStep = 1
        else:
            xStep = -1
        
        if col > self.col:
            yStep = 1
        else:
            yStep = -1
        
        xTemp, yTemp = self.row + xStep, self.col + yStep
        while(xTemp != row and yTemp != col):
            if (board[xTemp][yTemp] != None):
                return True
            xTemp, yTemp = xTemp + xStep, yTemp + yStep
        return False
           
    
class Rook(Piece):
    
    name = 'R'
    
    def moveIsValid(self, row, col, board):
        if not super(Rook, self).moveIsValid(row, col, board):
            return False
        
        if (row != self.row and col != self.col):
            return False
        
        return not self.__pathIsBlocked(row, col, board)

        
    def __pathIsBlocked(self, row, col, board):
        if row == self.row:
            if col > self.col + 1:
                step = 1
            elif col < self.col - 1:
                step = -1
            else: return False
            for j in range(self.col + step, col, step):
                if board[row][j] != None:
                    return True
        
        elif col == self.col:
            if row > self.row + 1:
                step = 1
            elif row < self.row - 1:
                step = -1
            else: return False
            for j in range(self.row + step, row, step):
                if board[j][col] != None:
                    return True
        return False
            
        
            