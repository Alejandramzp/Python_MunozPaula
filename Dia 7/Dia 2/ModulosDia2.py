
def fibonacci(n):        ## Definir la funciòn y agragarle el paràmetro de n nùmeros para el array  
    
    fibo = [0,1]               ## Nombramos la funciòn y le asignamos los primeros valores         
    for i in range(2,n):       ## for desde 2 hasta n

        seriefibo = fibo[i-1]+fibo[i-2]    ## Formula de la serie Fibonacci
        fibo.append(seriefibo)              ## Agregar valores en el array  
    
           
    return fibo       


def juegoAdivinar():  ## Definir la funciòn
    import random
    numeroSecreto = random.randint(1, 100)  ## Damos un rango de 1 hasta 100 para el nùmero aleatorio
    return numeroSecreto  ##retornamos el nùmero secreto