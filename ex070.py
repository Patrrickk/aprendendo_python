tot_gasto = mais_mil = mais_barato = cont = 0
nome_m_barato = ''
while True:
    nome_produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$ '))
    tot_gasto += preco
    cont += 1
    if cont == 1 or preco < mais_barato:
        mais_barato = preco
        nome_m_barato = nome_produto
    if preco > 1000:
        mais_mil += 1
    stop = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    while stop not in 'SN':
        stop = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if stop == 'N':
        break
print(f'O total de gasto foi R${tot_gasto}')
print(f'Total de {mais_mil} produtos que custam mais de R$1000')
print(f'O produto mais barato foi {nome_m_barato} que custa R${mais_barato}')
