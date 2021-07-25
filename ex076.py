listagem = ('Caderno', 22.98,
            'Notebook', 2029.98,
            'Celular', 445.35,
            'Computador', 1023.3,
            'Mochila', 65.99,
            'Iphone', 2222.32)
print('=' * 70)
print(f'{"LISTAGEM DE PREÇOS":^70}')
print('=' * 70)
for c in range(0, len(listagem), 2):
    print(f'{listagem[c]:.<50}R$', f'{listagem[c + 1]:>10.2f}')
print('=' * 70)
