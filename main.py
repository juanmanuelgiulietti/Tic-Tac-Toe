import random

def crearTablero():
    """
    La funcion crearTablero() crea una matriz con espacios vacios donde el usuario eligira donde insertar su X u O.
    """
    tablero = []
    for i in range(3):
        tablero.append([])
    return tablero

def elegirQuienComienza(usuario):
    """
    La funcion elegirQuienComienza() elige aleatoriamente quien es el primer jugador en colocar su marca en el tablero.
    """
    jugadores = ["{usuario}", "Computadora"]
    jugadores.insert(usuario, 0)
    comienza = random.choice(jugadores)
    return comienza

def elegirMarca():
    """
    La funcion elegirMarca() le da la opcion al usuario de elegir con que marca quiere jugar, X o O y valida que el usuario responda correctamente.
    """
    marca = str(input("Elige su marca para jugar (X o O): ")).lower
    while marca != "x" and marca != "o":
        print("Por favor ingrese una respuesta valida.")
        marca = str(input("Elige su marca para jugar (X o O): ")).lower
    return marca

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
    print(f"¡Hola! 👋 {usuario} . Bienvenido al juego de Tic - Tac - Toe. Buena suerte 🍀")
    
    marca = elegirMarca()
    print(f"Marca elegida para jugar: {marca}")
    comienza = elegirQuienComienza(usuario)
    print(f"Comienza a jugar: {comienza}")
    tablero = crearTablero()
    print(tablero)
main()