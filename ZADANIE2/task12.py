# <span>5&nbsp;128&nbsp;P</span>

a = str(input())
a = a.split('&nbsp;')
b = a[0].replace('<span>', '')

print(f"{int(b)}{int(a[1]) + 1}")
