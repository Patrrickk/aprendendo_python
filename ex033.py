n1 = int(input('Digite um número: '))
n2 = int(input('Mais um: '))
n3 = int(input('Outro: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n2:
    maior = n3
print(f'O maior valor = {maior} \nO menor valor = {menor}')
# if n1 < n2 and n1 < n3:
#     print(f'Menor número = {n1}')
# if n2 < n1 and n2 < n3:
#     print(f'Menor númemro = {n2}')
# if n3 < n1 and n3 < n2:
#     print(f'Menor númeor = {n3}')
# if n1 > n2 and n1 > n3:
#     print(f'Maior = {n1}')
# if n2 > n1 and n2 > n3:
#     print(f'Maior = {n2}')
# if n3 > n1 and n3 > n2:
#     print(f'Maior = {n3}')
