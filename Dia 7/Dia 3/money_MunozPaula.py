## ---------------------------------------------------
## ------------------- Ejercicio 1 -------------------
## ---------------------------------------------------

import ModulosDia3 as Money

money = int(input(""))
coins = Money.moneyChange(money)
coin = ((money // 10) + ((money % 10) // 5) + ((money % 10) % 5))
if money >= 1 and money <=1000 :

    print (coin,"=",coins)

else:
    print("No change money")

## REALIZADO POR PAULA ALEJANDRA MUÑOZ PEÑARANDA -- 1095953057
