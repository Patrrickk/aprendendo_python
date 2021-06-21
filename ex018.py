from math import sin, cos, tan, radians
angulo = int(input('ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O ângulo de {angulo}° tem:')
print(f'Seno = {seno:.2f} \nCosseno = {cosseno:.2f} \ntangente = {tangente:.2f}')
