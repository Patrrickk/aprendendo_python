# def soma(a, b):
#     print(f'A = {a} e B = {b}')
#     s = a + b
#     print(f'A soma A + B = {s}')
#
#
# # Programa Principal
# t = int(input('A: '))
# h = int(input('B: '))
# soma(b=t, a=h)
# soma(9, 2)

# def contador(* num):
#     tam = len(num)
#     print(f'Os valores {num} e tem o tanho de {tam}')
#
#
# contador(2, 5, 7, 3)
# contador(1, 3)

def dobra(ist):
    pos = 0
    while pos < len(ist):
        ist[pos] *= 2
        pos += 1
    print(ist)


valores = [5, 3, 2, 6, 7, 8]
dobra(valores)
