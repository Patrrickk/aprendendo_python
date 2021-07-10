n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))
sair = 'S'
while sair == 'S':
    print("""    [1] somar
    [2] Multiplicar
    [3] Maior
    [4] novos números
    [5] sair do programa""")
    opcao = int(input('Escolha uma: '))
    if opcao == 1:
        soma = n1 + n2
        print('=' * 40)
        print(f'A soma de {n1} e {n2} é = {soma}')
        print('=' * 40)
    elif opcao == 2:
        multiplicacao = n1 * n2
        print('=' * 40)
        print(f'A multiplicação de {n1} e {n2} é = {multiplicacao}')
        print('=' * 40)
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('=' * 40)
        print(f'Entre {n1} e {n2} o maior é {maior}')
        print('=' * 40)
    elif opcao == 4:
        print('NOVOS NÚMEROS')
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Outro valor: '))
    elif opcao == 5:
        sair = 'a'
    else:
        print('=' * 40)
        print(f'Opcão inválida, tente novamente!')
        print('=' * 40)
print('Finalizado, tenha uma boa noite')
