""" Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela
 começa ou não com o nome “SANTO”."""
cidade = str(input('Qual é o nome da sua Cidade: ')).upper().strip()
print('SANTO' in cidade[0:5])
