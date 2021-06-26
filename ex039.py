from datetime import date
ano_nasc = int(input('Qual é seu ano de nascimento: '))
ano = date.today().year - ano_nasc
if 0 < ano < 18:
    print('Você ainda vai se alistar no exército')
    print(f'Atualmente tem {ano} anos e ainda faltam {18 - ano} anos para seu alistamento OBRIGÁTORIO')
elif ano == 18:
    print(f'Você está hapto a se alistar, procure uma junta militar imediatamente!')
elif ano > 18:
    print('Infelizmente você já passou do prazo de alistamento')
    print(f'Seu prazo foi há {ano - 18} anos, deverá pagar uma multa')
elif ano <= -1:
    print(f'Você não possui idade e ainda faltam {18 - ano} anos para se alistar')
