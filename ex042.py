print('-=-' * 20)
print(f'{"Analisador=de=Triângulos":=^60}')
print('-=-' * 20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo: '))
c = float(input('Terceiro: '))
if a + b > c and a + c > b and b + c > a:
    print(f'É possível formar um triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO')
    elif a != b != c != a:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print(f'Não é possível formar um triângulo')
