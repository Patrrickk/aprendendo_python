def area(a, b):
    s = a * b
    print(f'A área de um terreno {a:.1f}x{b:.1f} é de {s:.1f}m²')


largura = float(input('largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)
