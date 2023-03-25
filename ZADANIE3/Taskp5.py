number = int(input())
sum = sum(map(int, str(number)))
last = number % 10
if sum % 3 == 0 and last % 2 == 0:
    print("Число делится!")
    print("Ответ:", number // 6)
else:
    print("Число не делится")