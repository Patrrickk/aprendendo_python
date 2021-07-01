n = int(input('a '))
primos = 0
n_primos = 0
for c in range(1, 11):
    if n % c == 0:
        primos += 1
    else:
        n_primos += 1
if primos == 2:
    print(f'O némero {n} é PRIMO')
else:
    print(f'O número {n} não é PRIMO')
