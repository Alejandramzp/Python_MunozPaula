
# Ejercicio 1 
def negate(num):
    return -num
    
def largue_num(num):
    return(num > 10000)    

# Ejercicio 3 
def ball_collide(collide):
    
    if collide:
        return True
    else:
        return False

# Ejercicio Clase
def calculoTotal(producto,cantidad,Diccionario):
    if producto in Diccionario["Productos"]:
    
        indicadorProducto = Diccionario["Productos"].index(producto)
        total = Diccionario["Precios"][indicadorProducto]
        total = total * cantidad
        return f"El valor a pagar por {cantidad} de {producto} es de { total }"
    else:
    
        print("Producto no disponible")
    
    
    
    
