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

# n = int(input('Quantos termos quer mostrar? '))
# t1 = 0
# t2 = 1
# cont = 3
# print('0 → 1', end='')
# while cont <= n:
#     t3 = t2 + t1
#     print(f' → {t3}', end='')
#     cont += 1
#     t1 = t2
#     t2 = t3
# print('FIM', end='')

tot_idade = man = woman = idade_woman = idade = 0
sexo = ' '
print('#' * 40)
print(f'{"CADASTRO DE PESSOAS":^40}')
print('#' * 40)
while True:
    idade_str = str(input('Digite sua idade: '))
    while idade_str.isnumeric() is not True:
        idade_str = str(input('Dados inválidos, tente novamente: Digite sua idade: '))
    idade = int(idade_str)
    sexo_t = ' '
    while sexo_t.isalpha() is not True:
        sexo_t = str(input('Sexo [M/F]: ')).upper()
        while sexo_t != 'M' and sexo_t != 'F':
            sexo_t = str(input('Dados Incorretos, tente de novo: Sexo [M/F]: ')).upper()
    sexo = str(sexo_t).upper()
    if sexo == 'M':
        man += 1
    elif sexo == 'F':
        woman += 1
        if idade < 20:
            idade_woman += 1
    if idade >= 18:
        tot_idade += 1
    print('-' * 40)
    stop = ' '
    while stop.isalpha() is not True:
        stop = str(input('Quer continuar? [S/N]: ')).upper()
        while stop != 'S' and stop != 'N':
            stop = str(input('Erro na digitação, tente novamente: Quer continuar? [S/N]: ')).upper()
    print('-' * 40)
    if stop == 'S':
        print('=' * 40)
        print('CADASTRE UMA NOVA PESSOA!')
        print('=' * 40)
    elif stop == 'N':
        break
print('=' * 40)
print('Cadastro Finalizado Com Sucesso!')
print('=' * 40)
print(f'Todal de pessoas com mais de 18 anos = {tot_idade}')
print(f'Homens cadastrados = {man}')
print(f'Mulheres cadastradas = {woman}')
print(f'Mulheres com menos de 20 anos = {idade_woman}')
