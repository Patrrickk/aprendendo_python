import emoji
real = float(input('Quanto de dinheiro você tem no cartão? R$: '))
dolar = real / 5.05
iene = real * 21.8799
euro = real * 0.1649
peso = real * 4.0133
print(f'Com R$ {real:.2f} é possível comprar')
print(f'US$ {dolar:.2f} (Dólar) \U0001f4b5')
print(f'¥ {iene:.2f} (Iene) \U0001f4b4')
print(f'€ {euro:.2f} (Euro) \U0001f4b6')
print(f'$ {peso:.2f} (Peso) \U0001f1ef\U0001f1f5')
