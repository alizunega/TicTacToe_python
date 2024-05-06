
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def dibujar_cuerpo():
    for i in range(3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        for j in range(3):
            print(f"|   {board[i][j]}   ", end="")
        print("|")
        print("|       |       |       |")
    print("+-------+-------+-------+")


dibujar_cuerpo()
