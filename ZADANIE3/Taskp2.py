total = int(input("Введите сумму оплаты:"))
hour = int(input("Который час?"))
if hour >= 10 and hour <=12:
    print(total / 2)
elif hour >=20 and hour <= 22:
    print(total / 4)
else:
    print(total)
    