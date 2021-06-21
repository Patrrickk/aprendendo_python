from random import sample
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo: '))
n3 = str(input('Terceiro:  '))
n4 = str(input('Quarto: '))

sortear = sample([n1, n2, n3, n4], k=4)
print(f'A ordem sorteada foi {sortear}')
