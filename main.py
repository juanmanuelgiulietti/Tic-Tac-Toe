
import random
import time

def verificarGanador(tablero):
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] != " ":
            return fila[0]
    for i in range(3):
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            return tablero[0][i]
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return tablero[0][2]
    return None

def cambioDeTurno(nuevoTurno, simbolo_1):
    if nuevoTurno == simbolo_1:
        print("🧍‍♂️ Turno del jugador")
        fila = int(input("Ingrese la fila en la que desea colocar su marca (0 a 2): "))
        while fila < 0 or fila > 2:
            print("Por favor ingrese una respuesta valida.")
            fila = int(input("Ingrese la fila en la que desea colocar su marca (0 a 2): "))
        columna = int(input("Ingrese la columna en la que desea colocar su marca (0 a 2): "))
        while columna < 0 or columna > 2:
            print("Por favor ingrese una respuesta valida.")
            columna = int(input("Ingrese la columna en la que desea colocar su marca (0 a 2): "))
    else:
        print("🤖 Turno de la computadora...")
        time.sleep(1)
        fila = random.randint(0, 2)
        columna = random.randint(0, 2)   
    return fila, columna

def posicionarMarca(tablero, fila, columna, turno, simbolo_1):
    while tablero[fila][columna] != " ":
        print("⚠️ Este espacio ya está ocupado.")
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
    print("✅ ¡Buena jugada!")
    time.sleep(0.5)

    if turno == "X":
        turno = "O"
    else:
        turno = "X"
    return tablero, turno

def comenzarJuego(jugadorComienza):
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
    return simbolo_2 if jugadorComienza == "Computadora" else simbolo_1

def elegirQuienComienza(usuario):
    return random.choice(["Computadora", usuario])

def crearEImprimirTablero():
    tablero = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    for fila_mostrar in tablero:
        fila_emojis = [celda.replace("X", "❌").replace("O", "🔵") for celda in fila_mostrar]
        print(" | ".join(fila_emojis))
    return tablero

def elegirSimbolo():
    simbolo_1 = str(input("Elige el simbolo con el que desea jugar (X o O): ")).upper()
    while simbolo_1 != "X" and simbolo_1 != "O":
        print("Por favor ingrese una respuesta valida.")
        simbolo_1 = str(input("Elige el simbolo con el que desea jugar (X o O): ")).upper()
    simbolo_2 = "O" if simbolo_1 == "X" else "X"
    return simbolo_1, simbolo_2

def darBienvenidaAlUsuario():
    usuario = str(input("Ingrese su nombre para empezar a jugar: ")).capitalize()
    while usuario == " ":
        print("Por favor ingrese una respuesta valida: ")
        usuario = str(input("Ingrese su nombre para empezar a jugar: ")).capitalize()
    return usuario

def main():
    usuario = darBienvenidaAlUsuario()
    print()
    print("🧠 Bienvenido a TIC - TAC - TOE 🧠")
    print(f"¡Hola! 👋 {usuario}. Buena suerte 🍀\n")
    tablero = crearEImprimirTablero()
    print()
    simbolo_1, simbolo_2 = elegirSimbolo()
    print(f"{usuario} juega con {simbolo_1},\nComputadora juega con {simbolo_2}\n")
    jugadorComienza = elegirQuienComienza(usuario)
    print(f"Jugador que comienza el juego: {jugadorComienza}")
    turno = indicarTurnos(jugadorComienza, simbolo_1, simbolo_2)
    print(f"Empieza a jugar: {turno}\n")

    fila, columna = comenzarJuego(jugadorComienza)
    tablero, turno = posicionarMarca(tablero, fila, columna, turno, simbolo_1)

    print("Tablero actualizado:")
    for fila_mostrar in tablero:
        fila_emojis = [celda.replace("X", "❌").replace("O", "🔵") for celda in fila_mostrar]
        print(" | ".join(fila_emojis))

    cantidadRondas = 1
    ganador = verificarGanador(tablero)
    if ganador:
        print(f"🎉 ¡Felicitaciones! El jugador con la marca {ganador} ha ganado la partida. 🏆")

    while (cantidadRondas < 9) and ganador is None:
        fila, columna = cambioDeTurno(turno, simbolo_1)
        tablero, turno = posicionarMarca(tablero, fila, columna, turno, simbolo_1)
        ganador = verificarGanador(tablero)
        print("\nTablero actualizado:")
        for fila_mostrar in tablero:
            fila_emojis = [celda.replace("X", "❌").replace("O", "🔵") for celda in fila_mostrar]
            print(" | ".join(fila_emojis))
        if ganador:
            print(f"🎉 ¡Felicitaciones! El jugador con la marca {ganador} ha ganado la partida. 🏆")
            break
        cantidadRondas += 1
        print(f"Se han jugado {cantidadRondas} ronda/s.")

    if not ganador:
        print("🤝 ¡Empate! No hubo ganador esta vez.")
main()
