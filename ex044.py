valor = float(input('Volor a ser pago: '))
print("""
[1] À vista dinheiro/cheque: 10% de desconto
[2] À vista no cartão: 5% de desconto
[3] Em até 2x no cartão sem juros
[4] 3x ou mais no cartão: 20% de juros""")
opcao = int(input('Escolha uma opção para pagamento: '))
if opcao == 1:
    desconto = valor - (valor * 10 / 100)
    print(f'Sua compra de {valor} vai custar R${desconto} no final.')
elif opcao == 2:
    desconto = valor - (valor * 5 / 100)
    print(f'Sua compra de {valor} vai custar R${desconto} no final.')
elif opcao == 3:
    desconto = valor / 2
    print(f'Sua compra será parcelada em 2x de {desconto} sem juros')
    print(f'Sua compra de {valor} vai custar R${desconto} no final.')
elif opcao == 4:
    x3 = int(input('Em quantas vezes: '))
    desconto = valor / x3
    juros = desconto + (desconto * 20 / 100)
    print(f'Sua compra será parcelada em {x3}x de {juros} com juros')
    print(f'Sua compra de {valor} vai custar R${juros * x3} no final.')
else:
    print('Opção Inválida, Tente novamente')
