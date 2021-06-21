n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'\033[1:35mA soma vale {s} \nO produto é {m} \nDivisão é {d:.2f}', end='')
print(f'A divisão inteira {di} \nPotência {e}')
