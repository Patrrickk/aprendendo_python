lista = list()
parent_es = 0
parent_di = 0
abrir = ''
fechei = ''
lista.append(str(input('Digite a expressão: ')).strip())
for c in lista:
    for letras in c:
        if letras in '()':
            parent_es += letras.count('(')
            parent_di += letras.count(')')
        if letras == '(':
            abrir = 'SIM'
        elif letras == ')':
            if abrir == 'SIM':
                fechei = 'SIM'
            else:
                fechei = 'NAO'
        if abrir == 'SIM' and fechei == 'SIM':
            abrir = 'NAO'
            fechei = 'NAO'
juntar_parent = parent_es + parent_di
if juntar_parent % 2 == 0 and\
        parent_di == parent_es and abrir == 'NAO':
    print(f'Sua expressão está válida!')
else:
    print(f'Sua expressão está errada!')
