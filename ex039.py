from datetime import date
sexo = str(input('Qual é seu sexo? [M/F]: ')).strip().lower()
ano_nasc = int(input('Qual é seu ano de nascimento: '))
ano = date.today().year - ano_nasc
if sexo[0] == 'm':
    print(f'Quem nasceu em {ano_nasc} tem {ano} anos em {date.today().year}.')
    if 0 < ano < 18:
        ano_de_alis = ano_nasc + 18
        print(f'Você ainda vai se alistar no exército em {ano_de_alis}')
        print(f'Atualmente tem {ano} anos e ainda faltam {18 - ano} anos para seu alistamento OBRIGÁTORIO')
    elif ano == 18:
        print(f'Você está hapto a se alistar, procure uma junta militar imediatamente!')
    elif ano > 18:
        ano_de_alis = ano_nasc + 18
        print(f'Infelizmente você já passou do prazo de alistamento, deveria ter se alistado em {ano_de_alis}')
        print(f'Seu prazo foi há {ano - 18} anos, caso não tenha se alistado você deverá pagar uma multa')
    elif ano <= -1:
        print(f'Você não possui idade e ainda faltam {18 - ano} anos para se alistar')
else:
    print('As mulheres estão isentas do Serviço Militar Obrigatório')
