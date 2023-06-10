import random

class TetrisGame:
    BoardWidth = 10
    BoardHeight = 20
    Speed = 300

    def __init__(self, parent, mainWindow):
        self.board = [[0] * TetrisGame.BoardWidth for _ in range(TetrisGame.BoardHeight)]
        self.curPiece = None
        self.curX = 0
        self.curY = 0
        self.isStarted = False
        self.isPaused = False
        self.numLinesRemoved = 0
        self.parent = parent

    def start(self):
        self.isStarted = True
        self.isPaused = False
        self.numLinesRemoved = 0
        self.board = [[0] * TetrisGame.BoardWidth for _ in range(TetrisGame.BoardHeight)]
        self.newPiece()

    def pause(self):
        self.isPaused = not self.isPaused

    def resume(self):
        if self.isPaused:
            self.isPaused = False

    def moveLeft(self):
        self.tryMove(self.curPiece, self.curX - 1, self.curY)

    def moveRight(self):
        self.tryMove(self.curPiece, self.curX + 1, self.curY)

    def moveDown(self):
        self.tryMove(self.curPiece, self.curX, self.curY - 1)

    def rotatePiece(self):
        self.tryMove(self.curPiece.rotateRight(), self.curX, self.curY)

    def dropPiece(self):
        newY = self.curY

        while newY > 0:
            if not self.tryMove(self.curPiece, self.curX, newY - 1):
                break
            newY -= 1

        self.pieceDropped()

    def pieceDropped(self):
        for i in range(4):
            x = self.curX + self.curPiece.x(i)
            y = self.curY - self.curPiece.y(i)
            self.board[y][x] = self.curPiece.shape()

        self.removeFullLines()

        if not self.isWaitingAfterLine:
            self.newPiece()

    def removeFullLines(self):
        numFullLines = 0
        rowsToRemove = []

        for i in range(TetrisGame.BoardHeight):
            if all(self.board[i]):
                rowsToRemove.append(i)

        for row in rowsToRemove:
            del self.board[row]
            self.board.insert(0, [0] * TetrisGame.BoardWidth)
            numFullLines += 1

        self.numLinesRemoved += numFullLines

    def newPiece(self):
        self.curPiece = Shape()
        self.curPiece.setRandomShape()
        self.curX = TetrisGame.BoardWidth // 2 + 1
        self.curY = TetrisGame.BoardHeight - 1 + self.curPiece.minY()

        if not self.tryMove(self.curPiece, self.curX, self.curY):
            self.isStarted = False

    def tryMove(self, newPiece, newX, newY):
        for i in range(4):
            x = newX + newPiece.x(i)
            y = newY - newPiece.y(i)
            if x < 0 or x >= TetrisGame.BoardWidth or y < 0 or y >= TetrisGame.BoardHeight or self.board[y][x] != 0:
                return False
        self.curPiece = newPiece
        self.curX = newX
        self.curY = newY
        return True

    def getBoard(self):
        return self.board

class Shape:
    Tetrominoe = [
        [ [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0] ], # I
        [ [1, 1], [1, 1] ],                                     # O
        [ [0, 1, 1], [1, 1, 0], [0, 0, 0] ],                     # S
        [ [1, 1, 0], [0, 1, 1], [0, 0, 0] ],                     # Z
        [ [1, 1, 1], [0, 1, 0], [0, 0, 0] ],                     # T
        [ [1, 1, 1], [0, 0, 1], [0, 0, 0] ],                     # L
        [ [1, 1, 1], [1, 0, 0], [0, 0, 0] ]                      # J
    ]

    def __init__(self):
        self.pieceShape = []
        self.setShape(0)

    def shape(self):
        return self.pieceShape

    def setShape(self, shape):
        self.pieceShape = Shape.Tetrominoe[shape]

    def setRandomShape(self):
        self.setShape(random.randint(0, len(Shape.Tetrominoe) - 1))

    def x(self, index):
        return self.pieceShape[index][0]

    def y(self, index):
        return self.pieceShape[index][1]

    def rotateRight(self):
        newShape = Shape()
        newShape.pieceShape = self.pieceShape.copy()

        for i in range(4):
            newShape.setX(i, self.y(i))
            newShape.setY(i, -self.x(i))

        return newShape

    def setX(self, index, x):
        self.pieceShape[index][0] = x

    def setY(self, index, y):
        self.pieceShape[index][1] = y
