from gameboard import Gameboard

# Conway's Game of Life
def main():
    row = int(input("Number of rows: "))
    column = int(input("Number of columns: "))
    board = Gameboard(row, column)
    board.generate()
    board.draw()
    showStatus(board)

    while chooseOption() != 'q':
        board.update()
        board.draw()
        showStatus(board)


# Show status of the game, number of generations and number of cells
def showStatus(board):
    print("Generation: ", board.generation, " Living cells: ", board.livingCells())


# Choose option for program
def chooseOption():
    option = input("(1) Enter to continue,  (2) 'q' to quit")
    return option


# Run main procedure
main()
