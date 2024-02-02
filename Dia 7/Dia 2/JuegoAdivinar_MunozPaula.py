## ---------------------------------------------------
## ------------------- Ejercicio 2 -------------------
## ---------------------------------------------------

import random  ## Importar el modulo nùmeros aleatorios

import ModulosDia2 as jueguito

intentos=10 

print("-------------Bienvenido al juego de adivina un nùmero aleatorio---------------")
print("")
print("En este juego interactivo deberas adivinar un nùmero entre 1 y 100")
print("solo cuentas con 10 intentos, pero no te preocupes, el juego te proporcionarà pistas indicando si el nùmero secreto es mayor o menor que el nùmero que digitaste")
print("")
print("¡Recuerda que solo tienes 10 intentos!")

numeroSec= jueguito.juegoAdivinar() ##llamando a la funciòn
inten = 0 
while intentos > 0:  ##Condiciòn de los intentos para seguir pidiendo el nùmero
    try:
        secreto = int(input("Ingresa el nùmero secreto: ")) ## Ingresar el nùmero 
    except ValueError:    ## Error por si se digita algo diferente a nùmeros
        print("Entrada no valida")   
        continue  ## Permite continuar el ciclo

    intentos -= 1 ## restar intentos
    inten += 1      ##sumar intentos
    if secreto > numeroSec: ## Condiciòn si es un nùmero menor
        print("El numero secreto es menor. Vuelve a intentarlo.")
        
    elif secreto < numeroSec: ## Condiciòn si es un nùmero mayor
        print("El nùmero secreto es mayor. Vuelve a intentarlo.")

    else: ## Resultado si se adivina el nùmero secreto
        resultado= """
         ***********************
         *      RESULTADO      *
         ***********************
         """
        print(resultado)
        print(f"¡FELICIDADES! Has adivinado el nùmero secreto  {numeroSec} en  {inten} intentos.")
print("No adivinaste el nùmero secreto :c, el nùmero secreto era",numeroSec) ##Resultado si no se adivina el nùmero

## Desarrollado por PAULA ALEJANDRA MUÑOZ PEÑARANDA - 1095953057