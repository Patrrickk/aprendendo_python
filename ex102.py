def fatorial(n=1, show=0):
    """
    -> Calcula o Fatarial de um número.
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostra ou não o calculo.
    :return: O valor do Fatorial de um número n.
    """
    fac = 1
    for c in range(1, n + 1):
        if show > 0:
            print(c, 'x' if c < n else '=', end=' ')
        fac *= c
    return fac


fatorial = fatorial(5, True)
print(fatorial)
