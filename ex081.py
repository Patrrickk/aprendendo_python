valores = list()
while True:
    valores.append(int(input('Digitee um valor: ')))
    stop = ' '
    while stop != 'S' and stop != 'N':
        stop = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if stop == 'N':

        break
valores.sort(reverse=True)
print(f'Foram digitados {len(valores)} valores')
print(f'Lista em ordem decrescente {valores}')
if 5 in valores:
    print(f'O valor 5 foi digitado e está dentro da lista na posição {valores.index(5)}')
else:
    print('O valor 5 não foi digitado')
