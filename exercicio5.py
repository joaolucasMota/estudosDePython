a = int(input("digite aqui o coeficinete A "))
b = int(input("digite aqui o coeficiente B "))
c = int(input("digite aqui o coeficiente C "))

delta = b * b - (4 * a * c)

x1 = (- b + (delta ** 0.5))/ (2 * a)

x2 = (- b -(delta ** 0.5))/ (2 * a)

print(x1)
print(x2)