# frase = 'CURSO EM VIDEO PYTHON'.split()
# frase = ''.join(frase)
# print(frase[len(frase)::-1])  # frase ao contrario
print('\033[1;32m=\033[m'*40)
print('Digite dois números e vou te informar todos os núemeros pares entre eles ')
print('\033[1;33m=\033[m'*40)
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
n3 = n1 % 2
n4 = n2 % 2

if n1 > n2:
    print(f'N3 {n3} \nN4 {n4}')
    if n3 == 0 and n4 == 0:
        print('okok')
        for c in range(n2, n1, 2):
            print(c)
