import math
from math import sin, cos, sqrt, pow, pi, asin, tan, log


x = 3.6

y = -4.1

z = 5

eq_1 = sqrt(sin(x + pi / 3) ** 2)

eq_2 = cos(tan(1/((z+1) ** (1/3))) ** 2)

eq = log(abs(y - eq_1) + eq_2)

print("eq = ", eq)
z = (asin(cos((x + sqrt(3) / 3) * pi)) + 1.2 *(sqrt(2 - cos ** 2 * y)))