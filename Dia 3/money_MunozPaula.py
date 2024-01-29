def moneyChange(money):
    return  [10] * (money // 10) + [5] * ((money % 10) // 5) + [1] * ((money % 10) % 5)

money = int(input(""))
coins = moneyChange(money)
coin = ((money // 10) + ((money % 10) // 5) + ((money % 10) % 5))
if money >= 1 and money <=1000 :

    print (coin,"=",coins)

else:
    print("No change money")

