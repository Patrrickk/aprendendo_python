metros = float(input('Valor em metro: '))
km = metros / 1000
hec = metros / 100
dam = metros / 10
dm = metros * 10
cen = metros * 100
mil = metros * 1000
print(f'O valor {metros}m corresponde:')
print(f'{km}km (Quilômetro)')
print(f'{hec}hm (Hectometro)')
print(f'{dam}dam (Decametro)')
print(f'{dm}dm (Decímetro)')
print(f'{cen}cm (Centímetro)')
print(f'{mil}mm (Milímetro)')
