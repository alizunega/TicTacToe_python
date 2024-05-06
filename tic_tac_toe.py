from random import randrange

# valor original de board
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


####################################################
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


####################################################
def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    lista_libres = make_list_of_free_fields(board)
    user_choice = int(input("Ingresa tu movimiento: "))
    print(user_choice)

    if user_choice in range(1, 10):
        for i in range(0, 3):
            for j in range(0, 3):
                if (i, j) in lista_libres and board[i][j] == user_choice:
                    board[i][j] = "O"
                else:
                    print(f"Ingrese un nuevo valor,{user_choice} este ya fue tomado")

    else:
        print("El movimiento debe ser un valor entre 1 y 9")
        print("Chequee el tablero para ver los casilleros ya asignados")

    display_board(board)


####################################################
def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos.
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    free_fields = []
    for i in range(0, 3):
        for j in range(0, 3):
            if isinstance(board[i][j], int):
                free_fields.append((i, j))

    return free_fields


####################################################
def victory_for(board, sign):
    win = False
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

    sign_list = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == sign:
                sign_list.append((i, j))

    for tupla in wins_tuples:
        if tupla in sign_list:
            if sign == "X":
                print("Has perdido")
                win = True
            elif sign == "O":
                print("Has ganado")
                win = True
            else:
                print("No hay ganador")
    return win


####################################################
def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    lista_libres = make_list_of_free_fields(board)
    mac_choice = randrange(1, 10)
    print(mac_choice)

    if mac_choice in range(1, 10):
        for i in range(0, 3):
            for j in range(0, 3):
                if (i, j) in lista_libres and board[i][j] == mac_choice:
                    board[i][j] = "X"
                else:
                    print("Valor ocupado, la maquina debe seleccionar uno nuevo")

    display_board(board)


###################### Principal ##############################

print("TIC-TAC_TOE")
display_board(board)
print("Deseas comenzar el juego??")
comienzo = input("Ingresa y para comenzar, o n para finalizar: ")
if comienzo.lower() == "y":
    board[1][1] = "X"
    free = []
    count = 1
    display_board(board)
    while count <= 5:  # controla que se haya hecho un minimo de movimientos
        enter_move(board)  # movimiento de usuario y actualiza
        draw_move(board)  # movimiento de maquina y actualiza
        count = +2

    free = make_list_of_free_fields(board)
    result = victory_for(board, "X")
    while not result:
        if free != []:
            enter_move(board)
            draw_move(board)
            result = victory_for(board, "X")
        else:
            print("No quedan movimientos por hacer")
else:
    print("Lamento que no quieras jugar")
