import random

def cambioDeTurno(nuevoTurno, simbolo_1):
    """
    La funcion cambioDeTurno(nuevoTurno, simbolo_1) cambia el turno y pide un nuevo ingreso.
    """
    if nuevoTurno == simbolo_1:
        fila = int(input("Ingrese la fila en la que desea colocar su marca (0 a 2): "))
        while fila < 0 or fila > 2:
            print("Por favor ingrese una respuesta valida.")
            fila = int(input("Ingrese la fila en la que desea colocar su marca (0 a 2): "))
        columna = int(input("Ingrese la columna en la que desea colocar su marca (0 a 2): "))
        while columna < 0 or columna > 2:
            print("Por favor ingrese una respuesta valida.")
            columna = int(input("Ingrese la columna en la que desea colocar su marca (0 a 2): "))
    else:
        fila = random.randint(0, 2)
        columna = random.randint(0, 2)   
    return fila, columna

def posicionarMarca(tablero, fila, columna, turno, simbolo_1):
    """
    La funcion posicionarMarca(tablero,fila,columna, turno) posiciona la marca correspondiente al turno en la posicion elegida por el usuario, y valida si esta está repetida o no. Por el lado de la computadora lo posiciona al azar. Una vez hecho esto cambia el turno.
    """
    while tablero[fila][columna] != " ":
        print("Este espacio ya está ocupado.")
        if turno == simbolo_1:
            fila = int(input("Ingrese la fila en la que desea colocar su marca (0 a 2): "))
            while fila < 0 or fila > 2:
                print("Por favor ingrese una respuesta válida.")
                fila = int(input("Ingrese la fila en la que desea colocar su marca (0 a 2): "))
            columna = int(input("Ingrese la columna en la que desea colocar su marca (0 a 2): "))
            while columna < 0 or columna > 2:
                print("Por favor ingrese una respuesta válida.")
                columna = int(input("Ingrese la columna en la que desea colocar su marca (0 a 2): "))
        else:
            fila = random.randint(0, 2)
            columna = random.randint(0, 2)
            
    tablero[fila][columna] = turno

    if turno == "X":
        turno = "O"
    else:
        turno = "X"
    return tablero, turno

def comenzarJuego(jugadorComienza):
    """
    La funcion comenzarJuego(jugadorComienza) evalua a quien le toca iniciar, si es el usuario le pide que ingrese la posicion donde quiere guardar su marca, y si es la computadora lo genera aleatoreamente.
    """
    if jugadorComienza == "Computadora":
        fila = random.randint(0, 2)
        columna = random.randint(0, 2)
    else:
        fila = int(input("Ingrese la fila en la que desea colocar su marca (0 a 2): "))
        while fila < 0 or fila > 2:
            print("Por favor ingrese una respuesta valida.")
            fila = int(input("Ingrese la fila en la que desea colocar su marca (0 a 2): "))
        columna = int(input("Ingrese la columna en la que desea colocar su marca (0 a 2): "))
        while columna < 0 or columna > 2:
            print("Por favor ingrese una respuesta valida.")
            columna = int(input("Ingrese la columna en la que desea colocar su marca (0 a 2): "))
    return fila, columna

def indicarTurnos(jugadorComienza, simbolo_1, simbolo_2):
    """
    La funcion indicarTurnos(jugadorComienza, simbolo_1, simbolo_2) define de quien es cada marca, y define cuando sera el turno de cada jugador.
    """
    if jugadorComienza == "Computadora":
        turno = simbolo_2
    else:
        turno = simbolo_1
    return turno
        
def elegirQuienComienza(usuario):
    """
    La funcion elegirQuienComienza(usuario) elige aleatoreamente mediante un random choice, que jugador comienza la partida.
    """
    jugadores = ["Computadora", usuario]
    jugadorComienza = random.choice(jugadores)
    return jugadorComienza

def crearEImprimirTablero():
    """
    La funcion crearTablero() crea una matriz con espacios vacios donde el usuario eligira donde insertar su X u O y la imprime.
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
    return simbolo_1, simbolo_2

def darBienvenidaAlUsuario():
    """
    La funcion darBienvenidaAlUsuario() pide al usuario ingresar su nombre y lo valida, para darle la bienvenida y comenzar el juego.
    """
    usuario = str(input("Ingrese su nombre para empezar a jugar: ")).capitalize()
    while usuario == " ":
        print("Por favor ingrese una respuesta valida: ")
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
    tablero = crearEImprimirTablero()
    print()
    simbolo_1, simbolo_2 = elegirSimbolo()
    print(f"{usuario} juega con {simbolo_1},\nComputadora juega con {simbolo_2}")
    print()
    jugadorComienza = elegirQuienComienza(usuario)
    print(f"Jugador que comienza el juego: {jugadorComienza}")
    print()
    turno = indicarTurnos(jugadorComienza, simbolo_1, simbolo_2)
    print(f"Empieza a jugar: {turno}")
    print()

    fila, columna = comenzarJuego(jugadorComienza)
    print()
    print(f"Fila elegida: {fila}\nColumna elegida: {columna}")
    print()

    tablero, turno = posicionarMarca(tablero, fila, columna, turno, simbolo_1)
    print("Tablero actualizado:")
    for fila_mostrar in tablero:
        print(fila_mostrar)

    cantidadRondas = 1
    print()
    print(f"Proximo turno: {turno}")
    print(f"Cantidad de rondas jugadas: {cantidadRondas}")
    print()

    while cantidadRondas < 9:
        fila, columna = cambioDeTurno(turno, simbolo_1)
        tablero, turno = posicionarMarca(tablero, fila, columna, turno, simbolo_1)
        
        print("Tablero actualizado:")
        for fila_mostrar in tablero:
            print(fila_mostrar)

        cantidadRondas += 1
        print(f"Se han jugado {cantidadRondas} ronda/s.")
main()