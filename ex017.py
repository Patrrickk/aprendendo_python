from math import hypot
oposto = float(input('Cateto oposto: '))
adjacente = float(input('Cateto adjacente: '))
hi = hypot(oposto, adjacente)
# hi = (co ** 2 + ca ** 2 ) ** (1/2)
print(f'A hipotenusa vai medir {hi:.2f}')
