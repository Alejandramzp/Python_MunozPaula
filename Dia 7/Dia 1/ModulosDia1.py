def Ejercicio1 ():
    ## ---------------------------------------------------
    ## ------------------- Ejercicio 1 -------------------
    ## ---------------------------------------------------

    # Impresión en consola
    print ("Hola Mundo")

    ##----------------- Datos Primitivos -----------------

    # 1. String
    texto = "Campus"
    print (texto)
    print(type(texto))

    # 2. Int
    numeroEntero = 6
    print(numeroEntero)

    # 3. Float
    numeroDecimal = 2.5
    print(numeroDecimal)

    # 4. Double
    numeroDecimalLargo = 3.1416346845246842346
    print(numeroDecimalLargo)

    # 5. Boolean
    booleano = True
    print(booleano)

    ## ---------- Entradas por parte del usuario ----------

    entradaUsuario = input("Ingresa tu nombre: ")
    print("Tu nombre es: ", entradaUsuario)

    ## --- Entradas por parte del usuario con definición de tipo de dato primitivo ---

    entradaUsuarioNumero = input("Ingresa tu edad: ")
    numeroFinal = int(entradaUsuarioNumero)
    print("Tu edad es: ", numeroFinal)

    ## --------------------- Ciclos -----------------------

    # Ciclo for
    for i in range (5,10,2): ## for contador in range(desde,hasta,pasos):
        print(i)

    # Ciclo while
    booleanito = True
    while booleanito == True: ##while condición_a_cumplir
        print("Sigo vivo")
        booleanito = False

    ## ----------------- Condicionales -------------------
        
    texto1 = "Campus"
    if texto1 == "Campus": ##if condicion_a_cumplir
        print("Soy Campus")
    else:                   
        print("No soy Campus")

    ##-------------------- Funciones ---------------------

    # 1. Con parámetros y con retorno
    def sumarNumeros(num1,num2):   ##def nombre_de_la_función y se le agrega los parámetros

        suma = num1 + num2                    ## Instrucciones
        print("La suma de los dos números es : ", suma,)
        return suma                 ##return + lo que desea que se retorne 
        
    num1 = int(input("Ingresa el número 1 :"))
    num2 = int(input("Ingresa el número 2 :"))

    sumarNumeros(num1, num2)   ##se llama a la función y los parámetros
        
    # 2. Sin parámetros y con retorno
    def multiplicaNumeros():            ##def nombre_de_la_función
        multiplicacion = a * b           ## Instrucciones
        print("La multiplicación de los dos números es: ", multiplicacion,)
        return multiplicacion           ##return + lo que desea que se retorne 

    a = int(input("Ingresa el número 1 :"))
    b = int(input("Ingresa el número 2 :"))   

    multiplicaNumeros()

    # 3. Con parámetros y sin retorno
    def saludoConNombre(nombre):  ##def nombre_de_la_función y se le agrega los parámetros
        print("Bienvenida " + nombre + " *-*")  ## Instrucciones

    saludoConNombre("Paula")  ##Se llama a la función para que muestre en la consol

    # 4. sin parámetros y sin retorno
    def saludar():     ##def nombre_de_la_función
        print("Holi")    ## Instrucciones

    saludar()       ##Se llama a la función para que muestre en la consola     

    ##-------------------- Arreglos ----------------------

    listaNombres = ["Roronoa Zoro","Christopher","Melody","Paula"]
    print("")

    print(listaNombres[0])
    print(listaNombres[1])
    print(listaNombres[2])
    print(listaNombres[3])

    ## Desarrollado por PAULA ALEJANDRA MUÑOZ PEÑARANDA - 1095953057
