n = contador = somatorio = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        contador += 1
        somatorio += n
print(f'Você digitou {contador} e a soma entre eles vale {somatorio}')
