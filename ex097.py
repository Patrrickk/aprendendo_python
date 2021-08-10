def mensagem(msg):
    tam = len(msg) + 2
    print('~' * tam)
    print(f'{msg:^{tam}}')
    print('~' * tam)


mensagem('Gustavo Guanabara')
mensagem('Curso de Python no Youtube')
mensagem('CeV')
mensagem('Boa noite, meu grande é nobre amigo!')
