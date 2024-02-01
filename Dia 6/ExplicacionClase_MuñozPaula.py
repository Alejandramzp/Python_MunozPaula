#Creación de Diccionario - {llave1:valor1,llave2:valor2}
Diccionario = {'Nombre':("Paula","Alejandra"),"Edad":25,"Barrio":"Brisas"}
print(Diccionario)
print(type(Diccionario))

#Buscar valor de x llave del diccionario y buscar 
#el segundo dato que contiene la subdiccionario
print(Diccionario['Nombre'][1])
Diccionario['Nombre']="Pau"
print(Diccionario)
print(type(Diccionario))
print(Diccionario['Nombre'])

#Recorrer un Diccionario por llaves
for i in Diccionario:
    print(i)

#Recorrer un Diccionario por valor 
for valor in Diccionario:
    print(Diccionario[valor])

#Imprimir las llaves y valores de un diccionario
for llave , valor in Diccionario.items():
    print(llave,valor)

#Limpiar un diccionario
print("############################")
#diccionario.clear() ---- OJOOOOOOOOO , RECUERDA QUE ESTO LIMPIA EL DICCIONARIO
print(Diccionario)

#Guardar las llaves de un diccionario en una lista
listaLlaves= Diccionario.keys()
print(listaLlaves)

#Guardar los valores de un diccionario en una lista
listaValores= Diccionario.values()
print(listaValores)

#Eliminar una llave de un diccionario
Diccionario.pop("Nombre")
print(Diccionario)

#Eliminar un elemento del diccionario de manera aleatoria
#diccionario.popitem()
print(Diccionario)

#Cruzar un diccionario a con uno b
diccionario2= {'Edad': 22, 'Barrio': 'Ruitoque'}
Diccionario.update(diccionario2)
print(Diccionario)

## Creado por PAULA ALEJANDRA MUÑOZ PEÑARANDA