import random
import time

print("Bienvenido al juego de las adivinanzas")
print("***** Las reglas son simples *****")
print()
print("Tienes que elegir un color, si la PC no ")
print("elige el mismo, ella gana 1 punto, si es")
print("el tuyo, tú ganas 3 puntos.")
print()
print("El juego se repite hasta que algún jugador")
print("llegue a 10 puntos o el jugador se retire.")
print()
print("************** ¡Jugamos! :) ***************")

colors = ["rojo", "azul", "verde", "amarillo", "naranja", "morado"]
jugando = True

while jugando:
    computer_score, player_score = 0, 0

    while computer_score < 10 and player_score < 10:
        valid = False
        
        while not valid:
            aux = input("Elige un color (rojo [0], azul [1], verde [2], amarillo [3], naranja [4], morado [5], salir [N]): ")
            
            if aux.lower() == "n":
                jugando = False
                break
            
            if not aux.isdigit() or not (0 <= int(aux) <= 5):
                print("Entrada no válida. Ingresa un número del 0 al 5 o 'N' para salir.")
            else:
                aux = int(aux)
                valid = True
                
        if not jugando:
            break

        player_choice = colors[aux]
        print(f"El usuario eligió el color: {player_choice}")

        computer_choice = random.choice(colors)
        print(f"La computadora eligió: {computer_choice}")

        if player_choice == computer_choice:
            player_score += 3
            print("¡Ganaste 3 puntos!")
        else:
            computer_score += 1
            print("La computadora gana 1 punto.")

        print(f"Puntuación - Jugador: {player_score}, Computadora: {computer_score}")

    if not jugando:
        break
    
    print("\nFin de la partida =D")

    if computer_score == player_score:
        print("El juego está empatado.")
    elif player_score > computer_score:
        print("<== ¡Usuario gana! ==>\nEl jugador es victorioso")
    else:
        print("\n<== La computadora gana ==>\nEl jugador ha sido derrotado")
    
    print("\nGracias por jugar.")
    
    aux = input("¿Quieres repetir? (Y/N): ")
    if aux.lower() == "n":
        jugando = False
    else:
        print("¡Reiniciamos! :D")
