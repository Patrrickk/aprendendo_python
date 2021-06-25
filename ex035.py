"""Exercício Python 35: Desenvolva um programa que leia o comprimento
 de três retas e diga ao usuário se elas podem ou não formar um triângulo."""
print('-=-' * 20)
print(f'{"Analisador=de=Triângulos":=^60}')
print('-=-' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo: '))
r3 = float(input('Terceiro: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print(f'É possível Formar um triângulo ')
else:
    print(f'Não é possível formar um triângulo')
