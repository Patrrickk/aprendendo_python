vel = float(input('Qual é a velocidade do seu carro: '))
multa = (vel - 80) * 7  # Calcula o valor da multa
if vel > 80:
    print(f'Você ultrapassou o limite de 80Km/h, e foi multado em R${multa}')
print('Tenha uma boa viagem!')
