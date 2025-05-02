import random

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

def darBienvenidaAlUsuario():
    """
    La funcion darBienvenidaAlUsuario() pide al usuario ingresar su nombre para darle la bienvenida y comenzar el juego.
    """
    usuario = str(input("Ingrese su nombre para empezar a jugar: "))
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
main()