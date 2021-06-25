"""Faça um programa que leia um ano qualquer
 e mostre se ele é BISSEXTO."""

ano = int(input('Digite um ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} \033[1:32mé BISSEXTO\033[m')
else:
    print(f'O ano de {ano} \033[1:31mnão é BISSEXTO')
