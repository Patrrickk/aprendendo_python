n = int(input('Digite um número: '))
primos = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[1:92m', end='')
        primos += 1
    else:
        print('\033[1:91m', end='')
    print(f'{c}', end=' ')
if primos == 2:
    print(f'\nO némero {n} é PRIMO por ser divisível 2 vezes')
else:
    print(f'\n\033[1:91mO número {n} não é PRIMO')
