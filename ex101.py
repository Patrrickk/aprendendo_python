from datetime import date


def voto(year):
    idade = date.today().year - year
    print(f'Com {idade} anos: ', end='')
    if 65 >= idade >= 18:
        print('VOTO OBRIGATÓRIO.')
    elif idade <= 18:
        print('NÃO VOTA.')
    elif idade > 65:
        print('VOTO OPCIONAL.')


ano = int(input('Em que ano você nasceu: '))
voto(ano)
