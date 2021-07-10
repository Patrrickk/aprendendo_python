frase = str(input('Digite uma frase: ')).strip().split()
juntar_frase = ''.join(frase).upper()
palindromo = juntar_frase[::-1]
if palindromo == juntar_frase:
    print(f'A frase {juntar_frase} e o mesmo que {palindromo} ao contrario é um PALÍNDROMO')
else:
    print(f'A frase digitada não é palíndromo')

# com for

frase = str(input('Digite uma frase: ')).strip().split()
juntar_frase = ''.join(frase).upper()
inverso = ''
for letra in range(len(juntar_frase) - 1, -1, -1):
    inverso += juntar_frase[letra]
if inverso == juntar_frase:
    print(f'A frase {juntar_frase} e o mesmo que {inverso} ao contrario é um PALÍNDROMO')
else:
    print(f'A frase digitada não é palíndromo')
