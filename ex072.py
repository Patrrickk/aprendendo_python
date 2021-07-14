extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
           'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete',
           'Dezoite', 'Dezenove', 'Vinte')
stop = ''
while True:
    num = int(input('Digite um número de 0 a 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {extenso[num]}')
        stop = ' '
        while stop not in 'SN':
            stop = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
        if stop == 'N':
            break
print('FIM')
