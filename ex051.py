termo = int(input('Termo da PA: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao + 1
for c in range(termo, decimo, razao):
    print(c, end=' → ')
print('ACABOU')
