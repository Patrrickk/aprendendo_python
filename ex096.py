def area(larg, comp):
    s = larg * comp
    print(f'A área de um terreno {larg:.1f}x{larg:.1f} é de {s:.1f}m²')


#  programa principal
print('-' * 10, 'CONTROLE DE TERRENOS', '-' * 10)
la = float(input('largura (m): '))
co = float(input('Comprimento (m): '))
area(la, co)
