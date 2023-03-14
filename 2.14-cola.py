coinreq = 50
print("Amount due: " + str(coinreq))
while coinreq > 0:
    amount = int(input("Insert Coin: "))
    if amount < coinreq:
        if amount == 25 or amount == 10 or amount == 5 :
            coinreq = coinreq - amount
            print("Amount due: " + str(coinreq))
    else :
        coinreq = coinreq - amount
        print("Amount owed: " + str(coinreq))