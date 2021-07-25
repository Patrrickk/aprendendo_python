valores = list()
while True:
    num = int(input('Digite um valor: '))
    if num in valores:
        print('\033[1:91mValor duplicado! Não vou adicionar!\033[m')
    else:
        print('\033[1:92mValor adicionado com sucesso\033[m')
        valores.append(num)
    stop = ''
    while stop.isalpha() is not True:
        while stop != 'S' and stop != 'N':
            stop = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if stop == 'N':
        break
valores.sort()
print(f'Você adicionau os valores {valores}')
