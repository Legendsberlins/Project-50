amount_due = 50

while amount_due > 0:
    print("Amount due: ", amount_due)

    coin = [25, 10, 5]
    coin_insert = int(input("Insert coin: "))
    if coin_insert in coin:
        amount_due = amount_due - coin_insert

change_owed = abs(amount_due)
print(amount_due)
