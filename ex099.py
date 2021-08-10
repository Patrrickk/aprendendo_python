from time import sleep


def maior(* m):
    maxx = 0
    print('-' * 60)
    print('Analisando os valores passados...')
    for pos, c in enumerate(m):
        if pos == 0:
            maxx = c
        else:
            if c > maxx:
                maxx = c
        print(c, end=' ')
        sleep(.5)
    print(f'Foram informados {len(m)} valores ao todo.')
    sleep(.2)
    print(f'O maior valor informado foi {maxx}')


maior(1, 2, 4, 5, 7, 8)
maior(2, 4, 6)
maior(9, 2, 4, 6, 1, 3, 77)
maior()
