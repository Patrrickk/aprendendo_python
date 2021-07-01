termo = int(input('Termo da PA: '))
razao = int(input('Razão: '))
for c in range(termo, termo+(10-1) * razao+1, razao):
    print(c)
