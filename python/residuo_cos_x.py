import math

import numpy as np


def fx(x):
    return np.cos(x)


def pn(x, n):
    acc = 0
    for i in range(0, n / 2):
        acc = acc + ((-1 ** (i / 2)) * (math.pow(x, 2 * i) / math.factorial(i * 2)))

    return acc


def roda_programa():
    erro = 10E-5

    for i in range(2, 10, 2):
        a = math.pow(math.pi / 4, i + 1) / math.factorial(i + 1)

        if a <= erro:
            print(f"i = {i}, assim para o grau é {i} e Erro = {a}")
            break
        else:
            print(f"Processando ==> n = {i}, assim o grau é {i} e Erro = {a}")




if __name__ == "__main__":
    roda_programa()
