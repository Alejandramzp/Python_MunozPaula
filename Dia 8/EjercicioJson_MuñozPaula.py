import json
from datetime import datetime

Import1 = open('data.json')
DatosJson = json.load(Import1)
 
## 1.Devuelve un listado con todos los pedidos que se han realizado mostrando0 en primer lugar los más recientes.
punto1 = '''
************************
*   LISTADO ORDENADO   *
************************    
'''
print(punto1)

orden = DatosJson['ventas']['pedidos']
ordenados= sorted(orden, key=lambda pedido: datetime.strptime(pedido['fecha'], "%Y-%m-%d"), reverse=True)
for i in ordenados:
  print(i)

## 2.Devuelve todos los datos de los dos pedidos de mayor valor.
punto2 = '''
************************
* PEDIDOS MAYOR VALOR  *
************************    
'''
print(punto2)

mayorValor = DatosJson['ventas']['pedidos']
mayor = sorted(mayorValor, key=lambda Valormayor:(Valormayor['total']), reverse=True)
print(mayor[0])
print(mayor[1])

## 3.Devuelve un listado con los identificadores de los clientes que han realizado algún pedido sin repetirlos.
punto3 = '''
********************************
*  LISTADO DE IDENTIFICADORES  *
********************************   
'''
print(punto3)

Id = []
listadoId = DatosJson['ventas']['pedidos']
for i in listadoId:
  Id.append(i["id_cliente"])
Id = set(Id)
print(Id)

## 4.Devuelve un listado de todos los pedidos durante el año 2017, cuya cantidad total sea superior a 500€.
punto4 = '''
************************
*  TOTAL MAYOR A 500€  *
************************
'''
print(punto4)

cont = 0
Listado2017 = []
for i in DatosJson["ventas"]["pedidos"]:
    if "2017" in DatosJson["ventas"]["pedidos"][cont]["fecha"]:
        if DatosJson["ventas"]["pedidos"][cont]["total"] > 500:
            Listado2017.append(i)
        cont += 1
    else:
        cont += 1

for j in Listado2017:
  print(j)

## 5.Devuelve un listado con el nombre y los apellidos de los comerciales que tienen una comisión entre 0.05 y 0.11.
punto5 = '''
************************
* LISTADO COMISIÓN   *
************************
'''
print(punto5)
comercial = 0
comerciales=DatosJson["ventas"]["comerciales"]
comerciales_seleccionados = [comercial for comercial in comerciales if 0.05 <= comercial["comision"] <= 0.11]
print("Los comerciales con comisión entre 0.05 y 0.11 son:")
for comercial in comerciales_seleccionados:
    nombre = comercial["nombre"]
    apellido1 = comercial["apellido1"]
    apellido2 = comercial.get("apellido2", "")  # Si no hay segundo apellido, se asigna una cadena vacía
    print(f"{nombre} {apellido1} {apellido2}")
    
## 6.Devuelve el valor de la comisión de mayor valor que existe en la tabla comercial.
punto6 = '''
***************************
* COMISIÓN DE MAYOR VALOR *
***************************
'''
print(punto6)

comisionMayor = []
for i in DatosJson["ventas"] ["comerciales"] :
    comisionMayor.append(i["comision"])
comisionMayor.sort(reverse=True)
print(comisionMayor[0])

## 7.Devuelve el identificador, apellido y nombre de aquellos clientes cuyo ciudad sea "Sevilla". 
punto7 = '''
************************************
* IDENTIFICADOR, APELLIDO Y NOMBRE *
************************************
'''
print(punto7)
conta = 0

clientes = DatosJson['ventas']['clientes']
ApellidoNombre=sorted(clientes, key=lambda ordenar: (ordenar["apellido1"],ordenar["nombre"]))
print(ApellidoNombre)
for i in DatosJson["ventas"]["clientes"]:

    if "Sevilla" in DatosJson["ventas"]["clientes"][conta]["ciudad"]:
      print("")
      
         

