a= input("Введите игру или 0")
games= []
while a != "0":
    if a in games:
        print("игра в списке")
    else:
        games.append(a)
    a = input("Введите игру или 0")
print(games)