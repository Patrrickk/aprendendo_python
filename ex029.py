vel = float(input('Qual é a velocidade do seu carro: '))
multa = (vel - 80) * 7
if vel > 80:
    print(f'Você atigiu o limite de 80Km/h, foi multado em R${multa}')
print('Tenha uma boa viagem!')
