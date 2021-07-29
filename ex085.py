pessoas = list()
pessoas.append([])
pessoas.append([])
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

# pessoas = list()
# dado = list()
# for c in range(0, 7):
#     n = int(input('Digite um valor: '))
#     if c <= 1:
#         dado.append(n)
#         pessoas.append(dado[:])
#         dado.clear()
#     if c >= 2:
#         if pessoas[0][0] % 2 == 0:
#             if n % 2 == 0:
#                 pessoas[0].append(n)
#             else:
#                 pessoas[1].append(n)
#         else:
#             if n % 2 == 1:
#                 pessoas[0].append(n)
#             else:
#                 pessoas[1].append(n)
# if pessoas[0][0] % 2 == 0:
#     print(f'Os valores pares digitados foram: {pessoas[0]}')
# if pessoas[1][0] % 2 == 1:
#     print(f'Os valores ímpares digitados foram: {pessoas[1]}')
#
