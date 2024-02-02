## ---------------------------------------------------
## ------------------- Ejercicio 1 -------------------
## ---------------------------------------------------

import ModulosDia4 as paress
            
T = int(input())
for case in range(T):
    n_k =input("")
    num = input("")
    n = 0
    k = 0
    l_n = list()
    n_kLista = n_k.split(' ')
    numLista = num.split(' ')
    n = int(n_kLista[0])
    k = int(n_kLista[1])
    for p in range(n):
        numero = int(numLista[p])
        l_n.append(numero)
    result = paress.pares(l_n, n, k)
    print ("Case {}:{}".format(case+1,result))


## Desarrollo por PAULA ALEJANDRA MUÑOZ PEÑARANDA -- 1095953057
