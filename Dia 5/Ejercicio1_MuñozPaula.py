## ---------------------------------------------------
## ------------------- Ejercicio 1 -------------------
## ---------------------------------------------------

def pares(l_n, n, k):
    pairs = set()
    for i in range(n):
        for j in range(i+1, n):
            if (l_n[i]+l_n[j]) % k == 0:
                pairs.add((min(l_n[i],l_n[j]), max(l_n[i],l_n[j])))
    return len(pairs)
            
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
    result = pares(l_n, n, k)
    print ("Case {}:{}".format(case+1,result))

## Diseñado por Paula Muñoz Y Brayan Lindarte                    