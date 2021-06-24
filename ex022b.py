nome = str(input('Digite seu nome Completo: ')).strip()
print(f'Seu nome tem ao todo {len(nome) - nome.count(" ")} letras')
print(f'Seu primeiro nome tem {nome.find(" ")} letras')
