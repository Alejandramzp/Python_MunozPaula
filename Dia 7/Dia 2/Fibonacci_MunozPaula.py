## ---------------------------------------------------
## ------------------- Ejercicio 1 -------------------
## ---------------------------------------------------

import ModulosDia2 as fibo  ## Retornar el array

print("-------Bienvenido a la serrie de Fibonacci-------")
print("La serie comienza con 0 y 1, y cada valor siguiente es la suma de los dos valores anteriores.")
print("----¡Recuerda que ingresas a la serie digitando un nùmero entero positivo y sales digitando 0!----")


rta = True    ##  Nombrar una variable para que cumpla un booleano
while  rta:    ## Mientras la variable sea verdadera seguira en el while
    try:          ## Pedir el nùmero de la serie
        n = int(input("Por favor digita la cantidad de nùmeros enteros que deseas en la serie de Fibonacci o por el contrario si deseas salir del programa: "))
        while n <0:      # Condiciòn para que el while siga pidiendo un nùmero correcto 
             print("¡Error! Digita un nùmero entero positivo") ## Mensaje de error si la condiciòn se cumple
             n= int(input("nùmero serie de Fibonacci: ")) ## Se vuelve a pedir n hasta qye sea mayor de 0

        if n ==0: ## Condiciòn para que salga del programa
                print("Saliste del programa con èxito")
                break
        else: 
                if n >0:  ##Condiciòn para que la variable booleano se convierta en falsa
                    rta= False
    except ValueError:  ## Para que no se pueda digitar valores diferentes a enteros positivos
        print("¡Error! Valor no vàlido")
   


while n!=0:       ## Mientras n sea mayor que 0 se muestra la serie
    print(fibo.fibonacci(n))
    while True:     ## While para que el programa se detenga cuando muestra la lista
            try:
                n = int(input("Por favor digita la cantidad de nùmeros enteros que deseas en la serie de Fibonacci o por el contrario si deseas salir del programa: ")) 
                if n < 0 :
                    print("¡Error! Digita un nùmero entero positivo")
                else:
                     break       
            except ValueError:
                print("¡Error! Valor no vàlido")
print("Saliste del programa con èxito")  

## Desarrollado por PAULA ALEJANDRA MUÑOZ PEÑARANDA - 1095953057
