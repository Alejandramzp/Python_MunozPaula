## ---------------------------------------------------
## ------------------- Ejercicio 3 -------------------
## ---------------------------------------------------

import math

def ball_collide():
    if distance<=radio_suma:
        return True
    else:
        return False

## coordenadas A
print("Ingresa las coordenadas y el radio de la bola A") 
coordinates =input("").split(" ")

p = coordinates
x1 = float(p[0])
y1 = float(p[1])
r1 = float(p[2])
coord1 = (x1,y1,r1)
listA =[coord1]

## coordenadas B
print("Ingresa las coordenadas y el radio de la bola B") 
coordinates =input("").split(" ")

q = coordinates
x2 = float(q[0])
y2 = float(q[1])
r2 = float(q[2])
coord2 = (x2,y2,r2)
listB =[coord2]

print("Coordenadas y el radio de la bola A son:",listA)
print("Coordenadas y el radio de la bola B son:",listB)

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
radio_suma = r1 + r2

print(ball_collide())

## Creado por PAULA ALEJANDRA MUÑOZ PEÑARANDA