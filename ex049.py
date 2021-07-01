print('=' * 30)
print(f'{"TABUADA":^30}')
print('=' * 30)
n = int(input('Digite um número: '))
print('_' * 30)
for c in range(1, 11):
    print(f'{n}  X  {c:2} = {n * c}')
