
class Piece:
    
    def __init__(self, color, xCoord, yCoord):
        self.color = color
        self.xPos, self.yPos = xCoord, yCoord
        
    def moveEval(self, x, y, board):
        if (x < 0 and x > 7) or (y < 0 and y > 7):
            return False
        if (x == self.xPos and y == self.yPos):
            return False
        if (board[x][y] != 0 and board[x][y].color() == self.color):
                return False



class Queen(Piece):
    
    def moveEval(self, x, y, board):
        if !super(Queen, self).moveEval(x, y, board):
            return False
        
        if abs(self.xPos - x) != abs(self.yPos - y) and \
        (x != self.xPos and y != self.yPos):
            return False
        
        return !self.checkIfObstruct(self, x, y, board)
    
    def __checkIfObstruct(self, x, y, board):
        if x == self.xPos:
            if y > self.yPos:
                step = 1
            else:
                step = -1
            for j in range(y, self.yPos, step):
                if board[x][j] != 0:
                    return True
            return False
        
        elif y == self.yPos:
            if x > self.xPos:
                step = 1
            else:
                step = -1
            for j in range(x, self.xPos, step):
                if board[j][y] != 0:
                    return True
            return False
        
        if x > self.xPos:
            xStep = 1
        else:
            xStep = -1
        
        if y > self.yPos:
            yStep = 1
        else:
            yStep = -1
        
        xTemp, yTemp = self.xPos + xStep, self.yPos + yStep
        while(xTemp != x and yTemp != y):
            if (board[xTemp][yTemp] != 0):
                return True
        return False
            
        
        
class Knight(Piece):
    
    def moveEval(self, x, y, board):
        if !super(Knight, self).moveEval(x, y, board):
            return False
        
        xDif, yDif = abs(self.xPos - x), abs(self.yPos - y)
        
        return (xDif == 2 and yDif == 1) or (xDif == 1 and yDif == 2)
        
    
class Bishop(Piece):
    
    def moveEval(self, x, y, board):
        if !super(Bishop, self).moveEval(x, y, board):
            return False
        
        if abs(self.xPos - x) != abs(self.yPos - y):
            return False
        
        return !self.checkIfObstruct(x, y, board)
        
    
    def __checkIfObstruct(self, x, y, board):
        if x > self.xPos:
            xStep = 1
        else:
            xStep = -1
        
        if y > self.yPos:
            yStep = 1
        else:
            yStep = -1
        
        xTemp, yTemp = self.xPos + xStep, self.yPos + yStep
        while(xTemp != x and yTemp != y):
            if (board[xTemp][yTemp] != 0):
                return True
        return False
           
    
class Rook(Piece):
    
    def moveEval(self, x, y, board):
        if !super(Rook, self).moveEval(x, y, board):
            return False
        
        if (x != self.xPos and y != self.yPos):
            return False
        
        return !self.checkIfObstruct(x, y, board)
        
    def __checkIfObstruct(self, x, y, board):
        if x == self.xPos:
            if y > self.yPos:
                step = 1
            else:
                step = -1
            for j in range(y, self.yPos, step):
                if board[x][j] != 0:
                    return True
        
        elif y == self.yPos:
            if x > self.xPos:
                step = 1
            else:
                step = -1
            for j in range(x, self.xPos, step):
                if board[j][y] != 0:
                    return True
        return False
            
        
            