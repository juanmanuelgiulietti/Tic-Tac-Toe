import random

def elegirQuienComienza(usuario):
    jugadores = ["Computadora", usuario]
    jugadorComienza = random.choice(jugadores)
    return jugadorComienza

def imprimirTablero():
    """
    La funcion crearTablero() crea una matriz con espacios vacios donde el usuario eligira donde insertar su X u O.
    """
    tablero = [[" ", " ", " "],
               [" ", " ", " "],
               [" ", " ", " "],]
    for fila in tablero:
        print(f"{fila}")
    return tablero

def elegirSimbolo():
    """
    La funcion elegirSimbolo() le da al usuario la opcion de elegir con que simbolo quiere jugar y valida su entrada.
    """
    simbolo_1 = str(input("Elige el simbolo con el que desea jugar (X o O): ")).upper()
    while simbolo_1 != "X" and simbolo_1 != "O":
        print("Por favor ingrese una respuesta valida.")
        simbolo_1 = str(input("Elige el simbolo con el que desea jugar (X o O): ")).upper()
        
    if simbolo_1 == "X":
        simbolo_2 = "O"
    else:
        simbolo_2 = "X"
        simbolo_1 = "O"
    return simbolo_1, simbolo_2

def darBienvenidaAlUsuario():
    """
    La funcion darBienvenidaAlUsuario() pide al usuario ingresar su nombre para darle la bienvenida y comenzar el juego.
    """
    usuario = str(input("Ingrese su nombre para empezar a jugar: ")).capitalize()
    return usuario
def main():
    """
    La funcion main() realiza la llamada a todas las funciones del programa para completar su funcionamiento.
    """
    usuario = darBienvenidaAlUsuario()
    print()
    print(f"¡Hola! 👋 {usuario} . Bienvenido al juego de Tic - Tac - Toe. Buena suerte 🍀")
    print()
    tablero = imprimirTablero()
    print()
    simbolo_1, simbolo_2 = elegirSimbolo()
    print(f"{usuario} juega con {simbolo_1},\nComputadora juega con {simbolo_2}")
    print()
    jugadorComienza = elegirQuienComienza(usuario)
    print(f"Jugador que comienza el juego: {jugadorComienza}")
main()