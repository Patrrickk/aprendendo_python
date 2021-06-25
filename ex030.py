n = int(input('Digite um número: '))
if n % 2 == 0:
    print(f'O número {n} é \033[1:32mPAR\033[m')
else:
    print(f'O número {n} é \033[1:33mÍMPAR')
