brasileirao = ('Palmeiras', 'Bragantino', 'Atlético-MG', 'Fortaleza', 'Athletico-PR', 'Bahia', 'Fluminense', 'Flamengo',
               'Santos', 'Atlético-GO', 'Ceará', 'Corinthians', 'Juventude', 'São Paulo', 'Internacional', 'América-MG',
               'Sport Recife', 'Cuiabá', 'Chapecoense', 'Grêmio')
print(f'Os primeiros cincos colocados: \n{brasileirao[0:5]}')
print(f'Os quatro últimos são: \n{brasileirao[-4:]}')
print(f'Em ordem alfabética: \n{sorted(brasileirao)}')
print(f'O time da Chapecoense está na posição: {brasileirao.index("Chapecoense") + 1}')
for pos, times in enumerate(brasileirao):
    print(f'{pos + 1} = {times}')