from datetime import date
ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano
categoria = ''
if idade < 10:
    categoria = 'MIRIM'
elif idade < 15:
    categoria = 'INFANTIL'
elif idade < 20:
    categoria = 'JUNIOR'
elif idade < 26:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'
print(f'Você tem {idade} anos de idade é pertence a categoria {categoria}')
