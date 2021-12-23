from random import randint
from cell import Cell

class Gameboard:

    # Constructor with instance-variables for generating the gameboard
    def __init__(self, rows, columns):
        self._rows = rows
        self._columns = columns
        self.generation = 0
        self._grid = self.initGrid(rows, columns)


    # Method for initializing grid
    def initGrid(self, columns, rows):
        grid = []
        for x in range(rows):
            grid.append([])
            for y in range(columns):
                grid[x].append(Cell())
        return grid


    # Generates the gameboard
    def generate(self):
        for row in self._grid:
            for cell in row:
                status = randint(0,2)
                if status < 2:
                    cell.setDead()
                else:
                    cell.setAlive()


    # Makes gameboard visible in terminal
    def draw(self):
        for i in range(8):
            print()
        for row in self._grid:
            print()
            for element in row:
                symbol = element.getSymbolStatus()
                print(symbol, end = "")
        print()


    # Find and returns number of living cells
    def livingCells(self):
        cellsAlive = 0
        for row in self._grid:
            for cell in row:
                if cell.isAlive():
                    cellsAlive += 1
        return cellsAlive


    # Updates board and status for all cells
    def update(self):
        deadToAlive = []
        aliveToDead = []
        self.generation += 1

        for y in range(len(self._grid)):
            for x in range(len(self._grid[y])):

                cell = self._grid[y][x]
                neighbours = self.findNeighbours(x, y)
                cellsAlive = self.getAliveNeighbours(neighbours)

                if cell.isAlive() and (cellsAlive < 2 or cellsAlive > 3):
                    aliveToDead.append(cell)

                if not cell.isAlive() and cellsAlive == 3:
                    deadToAlive.append(cell)

        self.changeStatus(deadToAlive, aliveToDead)


    # Change status from dead to alive
    def changeStatus(self, deadToAlive, aliveToDead):
        for cell in deadToAlive:
            cell.setAlive()
        for cell in aliveToDead:
            cell.setDead()


    # Return number of alive neighbours
    def getAliveNeighbours(self, neighbours):
        cellsAlive = 0
        for neighbour in neighbours:
            if neighbour.isAlive():
                cellsAlive += 1
        return cellsAlive


    # Find status for each neighbour
    def findNeighbours(self, row, column):
        neighbourList = []
        for i in range(-1, 2):
            for j in range (-1, 2):
                if not (row + i == row and column + j == column):
                    if not (row + i < 0 or column + j < 0
                                        or row + i > self._rows - 1
                                        or column + j > self._columns - 1):
                        neighbourList.append(self._grid[column + j][row + i])
        return neighbourList
