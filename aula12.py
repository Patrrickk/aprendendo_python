nome = str(input('Qual é seu nome: '))
if nome == 'Patrick':
    print('Olá, lindo')
elif nome == 'Lucas' or nome == 'Maria' or nome == 'Pedro':
    print('Vai tomar um banho')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('nomezin normal hein')
print(f'Tenha um bom dia, {nome}!')
