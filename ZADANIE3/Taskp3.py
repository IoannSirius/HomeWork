product1 = int(input())
product2 = int(input())
product3 = int(input())
all = product1 + product2 + product3
if product1 > product2 and product2 > product3:
    print("Акция")
    print("Сумма к оплате:", all / 3)
elif product1 < product2 and product2 < product3:
    print("Акция")
    print("Сумма к оплате:", all / 2)
else:
    print("К оплате"), all