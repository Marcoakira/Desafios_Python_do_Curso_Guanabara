# descobre o valor da hypotenuse ( hipotenusa)
from math import sqrt

n1 = float(input('digite o comprimento do cateto oposto '))
n2 = float(input('digite o comprimento do cateto adjacente '))
print(f'O valor da hipotenusa é {sqrt(n1*n1+n2*n2)}')