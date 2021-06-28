import math
print('~' * 40)
print('PROGRAMA DE CORVERSÃO DE BASE NÚMERICA')
print('~' * 40)
num = int(input('Digite um número inteiro: '))
print("""
[1] BINÁRIO
[2] OCTAL
[3] HEXADECIMAL""")
print('_' * 20)
opcao = int(input('Escolha uma opção: '))
base = ''
a = 0
if opcao == 1:
    a = bin(num)
    base = 'BINÁRIO'
elif opcao == 2:
    a = oct(num)
    base = 'OCTAL'
elif opcao == 3:
    a = hex(num)
    base = 'HEXADECIMAL'
else:
    print('Opcão Inválida! Tente novamente!')
if opcao == 1 or opcao == 2 or opcao == 3:
    print(f'{num} convertido para {base} é igua {a[2:]}')
