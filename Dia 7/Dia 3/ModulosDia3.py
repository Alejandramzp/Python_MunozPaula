
def moneyChange(money):
    return  [10] * (money // 10) + [5] * ((money % 10) // 5) + [1] * ((money % 10) % 5)