parada = 's'
maior = menor = contador = somatorio = 0
while parada == 's':
    b = int(input('Digite um número: '))
    contador += 1
    somatorio += b
    if contador == 1:
        maior = b
        menor = b
    else:
        if b > maior:
            maior = b
        if b < menor:
            menor = b
    parada = str(input('Quer continuar? [S/N]: ')).strip().lower()[0]
media = somatorio / contador
print(f'Você digitou {contador} números e a média dos valores é {media:.2f} '
      f'\nMaior número = {maior} \nMenor número = {menor}')
