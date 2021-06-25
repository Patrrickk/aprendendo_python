n1 = int(input('Digite um número: '))
n2 = int(input('Mais um: '))
n3 = int(input('Outro: '))

if n1 < n2 and n1 < n3:
    print(f'Menor número = {n1}')
if n2 < n1 and n2 < n3:
    print(f'Menor númemro = {n2}')
if n3 < n1 and n3 < n2:
    print(f'Menor númeor = {n3}')
if n1 > n2 and n1 > n3:
    print(f'Maior = {n1}')
if n2 > n1 and n2 > n3:
    print(f'Maior = {n2}')
if n3 > n1 and n3 > n2:
    print(f'Maior = {n3}')
