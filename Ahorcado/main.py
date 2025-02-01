from random_word import RandomWords
import random
import text as text



def seleccionar_idioma():
    print("Seleccione el idioma / Select the language:")
    print("1. Español")
    print("2. English")
    opcion = input("Ingrese el número de su opción / Enter the number of your option: ")
    if opcion == "1":
        return "es"
    elif opcion == "2":
        return "en"
    else:
        return "ff"



#Main
r = RandomWords()
jugando = True
vidas = text.lives


idioma = seleccionar_idioma()
while "ff" == idioma:
    idioma = seleccionar_idioma()





while jugando:
  
    cant = 6
    print(vidas[cant])


    if idioma == "en":
        palabra = r.get_random_word().lower()

        valido = set("")
        invalido = set("")
        muestra = "-"*len(palabra)

        print("The word is: "+muestra + "\n")
        print("Lives: " + str(cant) + "\n")


        while jugando:
            char = input("Type a letter: ")[0]
            print("\n") 
        
            if char.lower() in palabra:
                valido.add(char)

                for i, caracter in enumerate(palabra):  
                    if caracter == char:  
                        aux = muestra[:i] + char + muestra[i+1:]
                        muestra = aux
                    
            else:
               if not (char in invalido):
                cant = cant - 1 
                invalido.add(char)

            if cant != 0:
                print("The word is: "+muestra + "\n")
            else: 
                print("The word is: "+palabra + "\n")
            
            print(vidas[cant] + "\n")
            print("Valid: " + (str(valido) if valido else "{''}") + 
                " Invalid: " + (str(invalido) if invalido else "{''}") + 
                " You have " + str(cant) + " lives \n")


            if cant == 0:
                print(text.game_name)
                jugando = False
            elif muestra.lower() == palabra.lower():
                print(text.winner)
                jugando = False



        aux = input("¿You wanna play again? (Y/N): ")
        if aux.lower() == "n":
            print("Thank you for playing =D")
            break
        else:
            print("Get ready! :D")
            jugando = True


    else:
        palabra = text.palabras[random.randint(0, 199)].lower()


        valido = set("")
        invalido = set("")
        muestra = "-"*len(palabra)

        print("La palabra es: "+muestra + "\n")
        print("Vidas: " + str(cant) + "\n")


        while jugando:
            char = input("Ingrese un carácter: ")[0]
            print("\n") 
        
            if char.lower() in palabra:
                valido.add(char)

                for i, caracter in enumerate(palabra):  
                    if caracter == char:  
                        aux = muestra[:i] + char + muestra[i+1:]
                        muestra = aux
                    
            else:
               if not (char in invalido):
                cant = cant - 1 
                invalido.add(char)

            if cant != 0:
                print("La palabra es: "+muestra + "\n")
            else: 
                print("La palabra es: "+palabra + "\n")
            
            print(vidas[cant] + "\n")
            print("Valido: " + (str(valido) if valido else "{''}") + 
                " Invalido: " + (str(invalido) if invalido else "{''}") + 
                " Quedan " + str(cant) + " vidas \n")


            if cant == 0:
                print(text.nombre)
                jugando = False
            elif muestra.lower() == palabra.lower():
                print(text.ganaste)
                jugando = False



        aux = input("¿Quieres repetir? (Y/N): ")
        if aux.lower() == "n":
            print("Gracias por jugar =D")
            break
        else:
            print("¡Reiniciamos! :D")
            jugando = True
