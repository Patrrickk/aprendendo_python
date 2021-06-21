money = float(input('Preço do produto: '))
desc = money - (money * 5 / 100)
print(f'Com o desconto de 5% o preço cai para {desc:.2f}')
