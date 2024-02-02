## ---------------------------------------------------
## ------------------- Ejercicio 1 -------------------
## ---------------------------------------------------

##----------------------------------------------------
## CÓDIGO CON ERRORES
'''
def negate(num):
    return -num
    
def largue_num(num):
    rest = (num > 10000)           #1. SE DEBE RETORNAR EL RESULTADO

negate(b)                          #2.  DEFINIR LA VARIABLE B
neg_b = num                        #3.  RETORNAR LA FUNCIÓN NEGATE 
print 'b:' , b, 'neg_b:', neg_b    #4. LE FALTA LA ESTRUCTURA ADECUADA AL PRINT -- AGREGAR PARENTESIS

big = largue_num(b)
print"b is big:", big              #4. LE FALTA LA ESTRUCTURA ADECUADA AL PRINT -- AGREGAR PARENTESIS
'''
##----------------------------------------------------
## CÓDIGO SOLUCIÓN

import ModulosDia6 as negativo

b= 85    
neg_b = negativo.negate(b) 
print ('b:' , b, 'neg_b:', neg_b)   

big = negativo.largue_num(b)
print("b is big:", big)  

## Creado por PAULA ALEJANDRA MUÑOZ PEÑARANDA
