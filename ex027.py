"""Exercício Python 27: Faça um programa que leia o nome completo
 de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente."""

nome = str(input('Digite seu nome completo: ')).strip()
div = nome.split()
print(f'Primiero nome: {div[0]}')
print(f'Útimo nome: {div[-1]}')
