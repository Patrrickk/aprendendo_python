"""Exercício Python 31: Desenvolva um programa que pergunte a distância
 de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
  Km para viagens de até 200Km e R$0,45 parta viagens mais longas."""

viagem = float(input('Qual é a distância da viagem em Km: '))
#  preco = viagem * 0.50 if viagem <= 200 else viagem * 0.45
if viagem <= 200:
    preco = viagem * 0.50
else:
    preco = viagem * 0.45
print(f'O valor da passagem ficou em R${preco:.2f}')

