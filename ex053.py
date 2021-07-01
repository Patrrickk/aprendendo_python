frase = str(input('Digite uma frase: ')).strip().split()
juntar_frase = ''.join(frase)
palindromo = juntar_frase[len(juntar_frase)::-1]
if palindromo == juntar_frase:
    print(f'A frase {juntar_frase} e o mesmo que {palindromo} ao contrario')
print('FIM')
