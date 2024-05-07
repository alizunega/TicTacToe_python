from random import choice

# valor original de board
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


######################## Dibuja el tablero ############################
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


######################### Movimiento del usuario ###########################
def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    lista_libres = make_list_of_free_fields(board)
    user_choice = input("Ingresa tu movimiento: ")
    if user_choice.isdigit():
        user_choice = int(user_choice)

        if user_choice in range(1, 10):
            tomado = False
            for i in range(0, 3):
                for j in range(0, 3):
                    if (i, j) in lista_libres and board[i][j] == user_choice:
                        board[i][j] = "O"
                        print("Usuario Eligió: ", user_choice)
                        tomado = True
            if not tomado:
                print(f"Ingrese un nuevo valor,{user_choice} este ya fue tomado")
                enter_move(board)

        else:
            print("El movimiento debe ser un valor entre 1 y 9")
            enter_move(board)

    else:
        print("El movimiento debe ser un valor entre 1 y 9")
        print("Chequee el tablero para ver los casilleros ya asignados")
        enter_move(board)

    display_board(board)


######################### Lista de coordenadas libres ###########################
def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos.
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    free_fields = []
    for i in range(0, 3):
        for j in range(0, 3):
            if isinstance(board[i][j], int):
                free_fields.append((i, j))

    return free_fields


####################### Comprueba si alguien ganó #############################


def victory_for(board, sign):
    win = False
    # La función analiza el estatus del tablero para verificar si
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    wins_tuples = [
        [(0, 0), (1, 0), (2, 0)],
        [(0, 0), (0, 1), (0, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    sign_list = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == sign:
                sign_list.append((i, j))

    print(sign_list, sign)

    if len(sign_list) < 3:
        return win
    else:
        ganador = 0
        for fila in wins_tuples:
            contador = 0
            for elem in fila:
                if elem in sign_list:
                    contador += 1

            if contador >= 3:
                ganador += 1

        print("listas ganadoras: ", ganador)
        if ganador >= 1:
            win = True

    return win


######################## Movimiento de la máquina ############################
def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    lista_libres = make_list_of_free_fields(board)

    if lista_libres:  # Verificar si hay campos libres disponibles
        # Elegir aleatoriamente una casilla de la lista de campos libres
        i, j = choice(lista_libres)
        print("Maquina Eligió: ", board[i][j])
        board[i][j] = "X"
    else:
        print("No quedan movimientos por hacer")

    display_board(board)


###################### Principal ##############################

print("TIC-TAC_TOE")
display_board(board)
print("Deseas comenzar el juego??")
comienzo = input("Ingresa y para comenzar u otra tecla para finalizar: ")
if comienzo.lower() == "y":
    board[1][1] = "X"
    free = []
    display_board(board)

    free = make_list_of_free_fields(board)

    while free and not victory_for(board, "X") and not victory_for(board, "O"):
        enter_move(board)
        draw_move(board)
        free = make_list_of_free_fields(board)

    if victory_for(board, "X"):
        print("Has perdido!")

    elif victory_for(board, "O"):
        print("Has ganado!")

    if make_list_of_free_fields(board) == []:
        print("No quedan movimientos por hacer")
        print("El juego quedó empatado!")
else:
    print("Lamento que no quieras jugar")
