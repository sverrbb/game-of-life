#The class describes a cell in the simulation

class Cell:

    # Constructor - instance variable "status" showing whether or not cell is alive
    def __init__(self):
        self._status = False


    # Changes cell status to dead
    def setDead(self):
        self._status = False


    # Changes cell status to alive
    def setAlive(self):
        self._status = True


    # Checks if cell is alive or dead
    def isAlive(self):
        return self._status


    # Gets cells status-representation sign
    def getSymbolStatus(self):
        if self._status:
            return "O"
        else:
            return "."
