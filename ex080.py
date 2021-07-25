lista = list()
menor = maior = 0
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0:
        lista.append(n)
        print('Adicionado ao final da lista')
    if c == 1:
        if n > lista[0]:
            lista.append(n)
            print('Adicionado ao final da lista')
        else:
            lista.insert(0, n)
            print('Adicionado na posição 0 da lista')
    if c > 1:
        if n > maior:
            lista.append(n)
            print('Adicionado ao final da lista')
        if n < menor:
            lista.insert(0, n)
            print('Adicionado na posição 0 da lista')
        if maior > n > menor:
            if n < lista[1]:
                lista.insert(1, n)
                print('Adicionado na posição 1 da lista')
            elif n < lista[2]:
                lista.insert(2, n)
                print('Adicionado na posição 2 da lista')
            if c == 4:
                if n > lista[2]:
                    lista.insert(3, n)
                    print('Adicionado na posição 3 da lista')
    menor = min(lista)
    maior = max(lista)
print(f'Os valores digitados em ordem foram {lista}')
print(f'Os valores digitados em ordem foram {lista}')
