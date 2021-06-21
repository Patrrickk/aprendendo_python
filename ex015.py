day = int(input('Quantos dias alugados: '))
km = float(input('Km percorridos: '))
price_car = (day * 60) + (km * 0.15)
print(f'O preço a pagar é de R${price_car:.2f}')
