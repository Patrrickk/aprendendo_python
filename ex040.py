nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda: '))
media = (nota1 + nota2) / 2
print(f'Tirando {nota1} e {nota2}. O aluno tem a média {media}')
if media < 5:
    print('Você foi \033[1;91mREBROVADO!\033[m estude mais')
elif media < 7:
    print('Você está de \033[1;93mRECUPERAÇÃO!\033[m')
elif media >= 7:
    print('Você foi \033[1;92mAPROVADO!\033[m Parabéns!')
