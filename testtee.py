# frase = 'CURSO EM VIDEO PYTHON'.split()
# frase = ''.join(frase)
# print(frase[len(frase)::-1])  # frase ao contrario
# n = int(input('Digite um número para saber seu fatorial: '))
# cont = n
# fac = 1
# while cont > 0:
#     print(cont, end=' ')
#     print('x ' if cont > 1 else '= ', end='')
#     fac = fac * 5
#     cont -= 1
# print(f'{fac}')
# n = int(input('Digite um número: '))
# f = 1
# for c in range(n, 0, -1):
#     f *= c
#     print(f'{c}', end='')
#     print(' x ' if c > 1 else ' = ', end='')
# print(f'{f}', end='')

n = int(input('Quantos termos quer mostrar? '))
t1 = 0
t2 = 1
cont = 3
print('0 → 1', end='')
while cont <= n:
    t3 = t2 + t1
    print(f' → {t3}', end='')
    cont += 1
    t1 = t2
    t2 = t3
print('FIM', end='')
