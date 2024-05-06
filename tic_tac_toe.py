from random import randrange

# valor original de board
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
win = False


def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    b_board = board

    for i in range(3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        for j in range(3):
            print(f"|   {b_board[i][j]}   ", end="")
        print("|")
        print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.

    user_choice = int(input("Ingresa tu movimiento: "))

    if user_choice in range(1, 10):
        if user_choice in board:
            # asigno valor a lista
            print(user_choice)


def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos.
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    free_fields = []
    for i in range(0, 3):
        for j in range(0, 3):
            if isinstance(board[i][j], int):
                free_fields.append((i, j))

    print(free_fields)
    return free_fields


def victory_for(board, sign):
    # La función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    wins_tuples = [
        ((0, 0), (1, 0), (2, 0)),
        ((0, 0), (0, 1), (0, 2)),
        ((0, 0), (1, 1), (2, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2)),
        ((0, 2), (1, 1), (2, 0)),
    ]

    print("algo")


def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.

    print("algo")


print("TIC-TAC_TOE")
display_board(board)
print("Deseas comenzar el juego??")
comienzo = input("Ingresa y para comenzar, o n para finalizar: ")
if comienzo.lower() == "y":
    board[1][1] = "X"
    free_fields = make_list_of_free_fields(board)
    if free_fields == []:
        print("El juego terminó, no hay movimientos disponibles")
    else:
        display_board(board)
        enter_move(board)
