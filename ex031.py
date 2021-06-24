viagem = float(input('Qual é a distancia da viagem em Km: '))
if viagem <= 200:
    preco = viagem * 0.50
else:
    preco = viagem * 0.45
print(f'O valor da passagem ficou em {preco}')
