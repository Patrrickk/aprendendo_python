# nome = str(input('Qual é seu nome?: '))
# if nome == 'Patrick':
#     print('Que nome esplêndido!')
# else:
#     print('Seu nome é muito normal!!')
# print(f'Bom dia, {nome}')

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda: '))
media = (nota1 + nota2) / 2
if media >= 6:
    print(f'Parabéns!! você passou, sua média foi {media}')
else:
    print('Você está de recuperação')
#   print('PASSOU' if media >= 6 else 'REPROVOU')
