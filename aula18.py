# teste = list()
# teste.append('gustavo')
# teste.append(40)
# galera = list()
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste[:])
# print(galera)
# galera = [['joão', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade.')
galera = list()
dado = list()
totmai = 0
totmen = 0
for c in range(0, 3):
    dado.append(str(input('Qual é seu nome meu consagrado? ')))
    dado.append(int(input('sua idade? ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')
