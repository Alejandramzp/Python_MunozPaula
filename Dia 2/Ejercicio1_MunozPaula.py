## ---------------------------------------------------
## ------------------- Ejercicio 1 -------------------
## ---------------------------------------------------
def fibonacci(n):        ## Definir la funciòn y agragarle el paràmetro de n nùmeros para el array  
    
    fibo = [0,1]               ## Nombramos la funciòn y le asignamos los primeros valores         
    for i in range(2,n):       ## for desde 2 hasta n

        seriefibo = fibo[i-1]+fibo[i-2]    ## Formula de la serie Fibonacci
        fibo.append(seriefibo)              ## Agregar valores en el array  
    
           
    return fibo                          ## Retornar el array

print("-------Bienvenido a la serrie de Fibonacci-------")
print("La serie comienza con 0 y 1, y cada término siguiente es la suma de los dos anteriores.")
print("----¡Recuerda que ingresas a la serie digitando un nùmero entero positivo y sales digitando 0!----")


rta = True
while  rta:
    try:
        n= int(input("Por favor digita la cantidad de nùmeros enteros que deseas en la serie de Fibonacci o por el contrario si deseas salir del programa: "))
        while n <0:
             print("¡Error! Digita un nùmero entero positivo")
             n= int(input("numero"))
    except ValueError:
        print("caracter invalido")
    else:
        if n ==0:
         print("Saliste del programa con èxito")
         break
        else:
            if n >0:
                rta= False


while n!=0:
    print(fibonacci(n))
    while True:
            try:
                n = int(input("Por favor digita la cantidad de nùmeros enteros que deseas en la serie de Fibonacci o por el contrario si deseas salir del programa: ")) 
                if n < 0 :
                    print("¡Error! Digita un nùmero entero positivo")
                else:
                    print("Saliste del programa con èxito")
                    break
            except ValueError:
                print("¡Error! Valor no vàlido")


## Desarrollado por PAULA ALEJANDRA MUÑOZ PEÑARANDA - 1095953057