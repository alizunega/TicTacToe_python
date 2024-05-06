from tablero.py import *

##lista - tuplas de posibles wins 
wins_tuples = [((0,0),(1,0),(2,0)), |
               ((0,0),(0,1),(0,2)), |
               ((0,0),(1,1),(2,2)), |
               ((1,0),(1,1),(1,2)), |
               ((2,0),(2,1),(2,2)), |
               ((0,1),(1,1),(2,1)), |
               ((0,2),(1,2),(2,2)), |
               ((0,2),(1,1),(2,0))]

#tableero
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#diccionario de coordenadas - valor
coord_valor = {
    (0,0):board[0][0],
    (0,1):board[0][1],
    (0,2):board[0][2],
    (1,0):board[1][0],
    (1,1):board[1][1],
    (1,2):board[1][2],
    (2,0):board[2][0],
    (2,1):board[2][1],
    (2,2):board[2][2]
    }


#lista de casilleros tomados
#contiene el 5 porque por defecto la maquina lo ocupa
lista_ocupados = [5]
board[1][1] = "X"


#solicitud ingreso de valor y comprobacion
user_choice = int(input("Ingresa tu movimiento: "))

while user_choice in range(0,10):
    if user_choice not in lista_ocupados:
        #asigno valor a lista
        lista_ocupados.append(user_choice)
        #modifico el diccionario para que ahora pueda modificar el tablero
        for key, value in coord_valor.items():
            if value == user_choice:
                coord_valor[key] = "O"
            break
        
            
            
        
        
    
