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
bi = []
base = 0
if opcao == 1:
    base = 2
elif opcao == 2:
    base = 8
while True:
    if opcao == 1 or opcao == 2:
        n = num % base
        bi += [n]
        num = num // base
        if num == 0:
            break
    if opcao == 3:
        n = num % 16
        bi += [n]
        num = num // 16
        if num == 0:
            break
bi.reverse()
print(f'{num} corvertido para é igual a {bi}')
