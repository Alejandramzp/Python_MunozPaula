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
comerciales_seleccionados = [comercial for comercial in comerciales if 0.05 <= comercial["comisión"] <= 0.11]
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
    comisionMayor.append(i["comisión"])
comisionMayor.sort(reverse=True)
print(comisionMayor[0])

## 7.Devuelve el identificador, apellido y nombre de aquellos clientes cuyo ciudad sea "Sevilla". 
punto7 = '''
************************************
* IDENTIFICADOR, APELLIDO Y NOMBRE *
************************************
'''
print(punto7)

Sevilla = []
clientes = DatosJson["ventas"]["clientes"] 
for i in DatosJson["ventas"]["clientes"]:
  if i.get("ciudad")=="Sevilla":
    Sevilla.append(i)
    Sevilla = sorted(Sevilla, key = lambda cliente: (cliente["apellido1"], cliente["nombre"]))
    cont += 1
  else:
    cont += 1

for j in Sevilla:
  print(j["id"], j["apellido1"], j["nombre"])

## 8.Devuelve un listado los clientes que empiezan por A y terminan por n y los empiezan por P.
punto8 = '''
*****************************
* LISTADO DE CLIENTES A Y P *
*****************************
'''
print(punto8)

ListaAlfabeto = []
clientesAlfabeto= DatosJson["ventas"]["clientes"]

for i in clientesAlfabeto:
  Alfabeto =(i["nombre"])
  A=Alfabeto.startswith("A")
  N=Alfabeto.endswith("n")
  P=Alfabeto.startswith("P")

  if A==True and N==True:
    ListaAlfabeto.append(Alfabeto)
    cont +=1
  elif P==True:
     ListaAlfabeto.append(Alfabeto)
     ListaAlfabeto = sorted(ListaAlfabeto)
     cont +=1

for j in ListaAlfabeto:
  print(j)

## 9.Devuelve un listado los clientes que empiezan por A ordenados alfabéticamente.
punto9 = '''
**************************
* LISTADO DE CLIENTES A  *
**************************
'''
print(punto9)

listaA= []
ClientesA = DatosJson["ventas"]["clientes"] 

for i in ClientesA:
  inicialA= i["nombre"]
  iniA = inicialA.startswith("A")
  if iniA ==True:
    listaA.append(inicialA)
    listaA = sorted(listaA)
    cont += 1
  else:
    cont += 1
 
for j in listaA:
  print(j)  

## 10. Devuelve un listado con nombres de los comerciales que tienen apellido "Ruiz" sin repetir.
punto10 = '''
**************************
* LISTADO DE CLIENTES A  *
**************************
'''
print(punto10)

apellidoRuiz= []
comerciales = DatosJson["ventas"]["comerciales"]

for i in comerciales:
  if i.get("apellido1")== "Ruiz":
    Ruiz = i["nombre"] + " " + i["apellido1"]
    apellidoRuiz.append(Ruiz)
    apellidoRuiz = sorted(apellidoRuiz)
    apellidoRuiz = set(apellidoRuiz)
    
for j in apellidoRuiz :   
  print(j)
