print(f"{'CALCULADORA DE IMC':^51}")
print('=' * 51)
print("""    IMC          CLASSIFICAÇÃO	    OBESIDADE (GRAU)
MENOR QUE 18,5	    MAGREZA	            0
ENTRE 18,5 E 24,9	NORMAL	            0
ENTRE 25,0 E 29,9	SOBREPESO	        I
ENTRE 30,0 E 39,9	OBESIDADE	        II
MAIOR QUE 40,0	    OBESIDADE GRAVE	    III""")
print('=' * 51)
sabe = str(input('Você sabe o que significa \033[1:93mIMC\033[m? (sim/não) ')).strip().strip().lower()
if sabe[0] in 's':
    print('Ok, vamos seguir')
elif sabe[0] in 'nñ':
    print('O IMC é a sigla para Índice de Massa Corpórea, parâmetro adotado pela Organização Mundial de Saúde para '
          'calcular o peso ideal de cada pessoa.')
else:
    print('não era essa a resposta, mas OK')
peso = float(input('Qual é seu peso?(kg) '))
altura = float(input('E sua altura?(m) '))
imc = peso / (altura * altura)
clas = ''
cor = 0
if imc < 18.5:
    clas = 'MAGREZA'
    cor = 1
elif imc < 25:
    clas = 'NORMAL'
    cor = 2
elif imc < 30:
    clas = 'SOBREPESO'
    cor = 3
elif imc < 40:
    clas = 'OBESIDADE'
    cor = 4
elif imc >= 40:
    clas = 'OBESIDADE GRAVE, cuidado!'
    cor = 5
verde = {1: '\033[92m', 0: '\033[m', 'limpa': '\033[m'}
print('-' * 51)
print(f'{verde[1]}Seu imc é de {imc:.2f}! Que é considerado {clas}{verde["limpa"]}')
print('-' * 51)
print('=' * 51)
print(f"""    IMC          CLASSIFICAÇÃO	    OBESIDADE (GRAU)
{verde[1 if cor == 1 else 0]}MENOR QUE 18,5	    MAGREZA	            0{verde["limpa"]}
{verde[1 if cor == 2 else 0]}ENTRE 18,5 E 24,9	NORMAL	            0{verde["limpa"]}
{verde[1 if cor == 3 else 0]}ENTRE 25,0 E 29,9	SOBREPESO	        I{verde["limpa"]}
{verde[1 if cor == 4 else 0]}ENTRE 30,0 E 39,9	OBESIDADE	        II{verde["limpa"]}
{verde[1 if cor == 5 else 0]}MAIOR QUE 40,0	    OBESIDADE GRAVE	    III{verde["limpa"]}""")
print('=' * 51)
