from gameboard import Tablero
import random


def seleccionar_idioma():
    # Selecciona el idioma del juego / Select the game language
    while True:
        print("Seleccione el idioma / Select the language:")
        print("1. Español")
        print("2. English")
        opcion = input("Ingrese el número de su opción / Enter the number of your option: ").strip()
        if opcion == "1":
            return True  # Español / Spanish
        elif opcion == "2":
            return False  # Inglés / English
        else:
            print("Opción inválida, intente nuevamente / Invalid option, try again.")


def nro(idioma):
    # Pide un número entre 1 y 3 / Ask for a number between 1 and 3
    mensaje = "Elige un número (1-3): " if idioma else "Choose a number (1-3): "
    error = "Entrada inválida. Ingresa un número válido entre 1 y 3." if idioma else "Invalid input. Please enter a valid number between 1 and 3."

    while True:
        num = input(mensaje).strip()
        if num.isdigit() and 1 <= int(num) <= 3:
            return int(num) - 1  # Convierte a índice de lista (0-2) / Convert to list index (0-2)
        else:
            print(error)


def posicion(idioma, pc):
    # Obtiene la posición del jugador o genera una aleatoria para la PC /
    # Get the player's position or generate a random one for the PC
    if pc:
        posX = random.randint(0, 2)
        posY = random.randint(0, 2)
    else:
        print("Elige una fila: ") if idioma else print("Choose a row: ")
        posX = nro(idioma)
        print("Elige una columna: ") if idioma else print("Choose a column: ")
        posY = nro(idioma)

    return posX, posY


# Inicio del juego / Game start
print("Bienvenido al TA-TE-TI / Welcome to Tic-Tac-Toe")
solo = input("¿Juegas solo? (Enter para sí, cualquier tecla para no) / Playing solo? (Press Enter for yes, any key for no): ") == ""
idioma = seleccionar_idioma()



board = Tablero()
fin = False
x = 0
o = 0

print("")
print("")

while not fin:
    # Reinicia el tablero / Reset the board
    board.clearboard()
    jugando = True
    jugada = "O"

    while jugando and not fin:
        # Alterna turnos entre X y O / Alternate turns between X and O
        jugada = "X" if jugada == "O" else "O"
        pc = solo and jugada == "O"  # La PC juega si es un juego solitario / PC plays if it's a solo game

        print("Es el turno de las " + jugada) if idioma else print("Now " + jugada + " is playing")

        correcto = False
        while not correcto:
            # Pide posición y verifica si está libre / Ask for position and check if it's free
            posX, posY = posicion(idioma, pc)
            correcto = board.add_movement(posX, posY, jugada)

            if not correcto and not pc:
                print("La posición está ocupada.") if idioma else print("The position is occupied.")

        board.print_board()

        # Verifica si hay un ganador / Check if there's a winner
        if board.is_game_won(jugada):
            print(f"El ganador es {jugada}") if idioma else print(f"{jugada} wins")
            if jugada == "O":
                o += 1
            else:
                x += 1
            jugando = False

        # Verifica si el tablero está lleno y reinicia / Check if the board is full and reset
        if board.is_board_full() and jugando:
            print("El tablero está lleno, reiniciando.") if idioma else print("The board is full, restarting.")
            board.clearboard()

    # Muestra el puntaje / Show the score
    print(f"Puntaje X: {x} y puntaje O: {o}") if idioma else print(f"Score X: {x}, Score O: {o}")

    # Pregunta si quieren seguir jugando / Ask if they want to keep playing
    aux = input("¿Quieres repetir? (Y/N): " if idioma else "Wanna play again? (Y/N): ").strip().lower()
    if aux == "n":
        fin = True
    else:
        print("¡Reiniciamos! :D" if idioma else "Restarting! :D")
