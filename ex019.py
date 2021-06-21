from random import choice
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo: '))
aluno3 = str(input('Terceiro: '))
aluno4 = str(input('Quarto: '))

sorteio = choice([aluno1, aluno2, aluno3, aluno4])
print(f'O aluno(a) sorteado foi {sorteio}')
