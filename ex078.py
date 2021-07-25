lista = list()
menor = maior = 0
menor_lista = list()
maior_lista = list()
for c in (range(0, 5)):
    lista.append(int(input(f'Digite um valor para a posição {c}: ')))
    menor = min(lista)
    maior = max(lista)
for pa, c in enumerate(lista):
    if menor == c:
        menor_lista.append(pa)
    if maior == c:
        maior_lista.append(pa)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições', *maior_lista, sep=', ')
print(f'O menor valor digitado foi {menor} nas posições', *menor_lista, sep=', ')
