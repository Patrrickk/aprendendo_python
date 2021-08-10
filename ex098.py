from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo -= passo * 2
    if passo == 0:
        passo = 1
    print('=-=' * 10)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if fim > inicio and passo > 0:
        fim += 1
    elif fim < inicio and passo > 0:
        fim -= 1
        passo -= (passo * 2)
    for cont in range(inicio, fim, passo):
        print(cont, end=' ')
        sleep(.1)
    print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
inicioo = int(input('Início: '))
fimm = int(input('Fim: '))
passoo = int(input('Passo: '))
contador(inicioo, fimm, passoo)
