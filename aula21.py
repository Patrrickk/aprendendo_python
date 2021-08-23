# def contador(i, f, p):
#     """
#     → Faz uma contagem e mostra na tela.
#     :param i: início da contagem
#     :param f: Fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno
#     Função criada por Patrick F.
#     """
#     c = i
#     while c <= f:
#         print(f'{c}', end=' ')
#         c += p
#     print('FIM!')
#
#
# help(contador)
# def funcao():
#     global n1
#     n1 = 2
#     print(f'N1 dentro vale {n1}')
#
#
# n1 = 4
# funcao()
# print(f'N1 fora vale {n1}')

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(4, 6, 1)
r2 = somar(1, 2)
r3 = somar(6, 3)

print(f'Os resultados valem {r1}, {r2}, {r3}')
