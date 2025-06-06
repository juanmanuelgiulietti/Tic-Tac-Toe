# 🧠 Tic Tac Toe - Juego en Python

Este proyecto es una versión en consola del clásico juego **Tic Tac Toe** (también conocido como Tres en Línea o Ta-Te-Ti), donde el jugador compite contra la computadora. El objetivo es alinear tres marcas iguales (❌ o 🔵) en una fila, columna o diagonal.

---

## 🎮 Cómo jugar

1. **Inicio del juego**:
   - Se solicita al usuario su nombre.
   - Luego elige su símbolo: ❌ (X) o 🔵 (O).
   - El juego elige aleatoriamente quién comienza la partida (jugador o computadora).

2. **Turnos**:
   - El jugador ingresa las coordenadas (fila y columna) donde desea colocar su marca.
   - La computadora elige posiciones aleatorias.
   - Si la celda ya está ocupada, se solicita otra posición.

3. **Final del juego**:
   - Gana quien alinee tres símbolos.
   - Si se llenan las 9 casillas sin ganador, el resultado es empate.

---

## 🧩 Estructura del Código

El código está dividido en funciones principales:

| Función | Descripción |
|--------|-------------|
| `darBienvenidaAlUsuario()` | Solicita y valida el nombre del jugador. |
| `elegirSimbolo()` | Permite al jugador elegir su símbolo (X u O). |
| `elegirQuienComienza(usuario)` | Determina aleatoriamente quién comienza. |
| `crearEImprimirTablero()` | Crea el tablero vacío e imprime su estado inicial. |
| `comenzarJuego(jugadorComienza)` | Primer movimiento del jugador o computadora. |
| `indicarTurnos(jugadorComienza, simbolo_1, simbolo_2)` | Define el símbolo de quien empieza. |
| `cambioDeTurno(nuevoTurno, simbolo_1)` | Administra el turno actual (jugador o computadora). |
| `posicionarMarca(tablero, fila, columna, turno, simbolo_1)` | Coloca la marca si el espacio está libre. |_

Desarrollado por Juan Manuel Giulietti
🔗 Repositorio GitHub: https://github.com/juanmanuelgiulietti/Tic-Tac-Toe.git