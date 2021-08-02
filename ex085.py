pessoas = [[], []]
for c in range(0, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        pessoas[0].append(n)
    elif n % 2 == 1:
        pessoas[1].append(n)
pessoas[0].sort()
pessoas[1].sort()
print(f'Os valores pares digitados foram: {pessoas[0]}')
print(f'Os valores ímpares digitados foram: {pessoas[1]}')
