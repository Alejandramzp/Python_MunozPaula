## ---------------------------------------------------
## ----------------- Ejercicio Clase------------------
## ---------------------------------------------------

#REALIZAR UN PROGRAMA QUE USE UN DICCIONARIO PARA GESTIONAR LOS PRODUCTOS
#Y PRECIOS DE LA TABLA, DONDE SE LE PREGUNTE AL USUARIO POR UN PRODUCTO
#Y LA CANTIDAD. AL FINALIZAR MOSTRAR EN LA CONSOLA EL PRECIO TOTAL. SI
#EL PRODUCTO NO ESTA DEBE MOSTRAR UN MENSAJE INFORMANDO SOBRE ELLO

Diccionario = {"Productos":("Cafe","Chocorramo","Cocacola","Gansito","Ponymalta","Empanada"),
               "Precios":(2500, 3000, 2000, 2200, 2800, 3500)}

print("----------Menú--------")

for i in range (5):
    print(Diccionario["Productos"][i]) 
    print("------------------",Diccionario["Precios"][i])
    
producto = str(input("Ingresa el producto que deseas comprar: "))
producto = producto.capitalize()
cantidad = int(input("Ingrese la cantidad que desea de este producto: "))

if producto in Diccionario["Productos"]:
    
    indicadorProducto = Diccionario["Productos"].index(producto)
    total = Diccionario["Precios"][indicadorProducto]
    total = total * cantidad
    print("El valor a pagar por",cantidad,producto,"es de:",total)
    
else:
    
    print("Producto no disponible")
    
    

## Creado por PAULA ALEJANDRA MUÑOZ PEÑARANDA