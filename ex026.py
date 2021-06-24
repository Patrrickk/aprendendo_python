frase = str(input('Escrevar uma frase: ')).lower().strip()
print(f"A letra A apareceu {frase.count('a')} vezes")
print(f'A primeira letra A apareceu na posição: {frase.find("a") + 1}')
print(f"A útima letra A apareceu na posição: {frase.rfind('a') + 1}")
