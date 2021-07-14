from random import randint
nus = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior = menor = 0
for cont, c in enumerate(nus):
    if cont == 0:
        maior = c
        menor = c
    else:
        if c > maior:
            maior = c
        if menor > c:
            menor = c
print(nus)
print(f'O Maior valor sorteado = {maior}\nO Menor valor sorteado = {menor}')
