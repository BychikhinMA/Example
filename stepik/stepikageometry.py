from math import cos, sqrt, pi, asin


x = float(input())
y = float(input())

eq1 = asin(cos((x + ((sqrt(3) / 2) * pi))))
eq2 = 1.2 * sqrt(2 - pow(cos(y), 2))
eq3 = x ** 2 + y ** 2 + 1
z = (eq1 + eq2) / eq3

print(round(z, 5))
