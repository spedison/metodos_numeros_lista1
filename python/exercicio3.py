import math
import numpy as np

def calculaF(x):
    return np.sin(x)

def ajusta_x_calculo_seno(x):
    ## Retorna o intervalo entre 0 PI/2 e o sinal que ele deve ser
    # multiplicado no final. Ex.:[1.45,-1]
    PI2 = math.pi * 2.
    sinal = 1. if (x > 0) else -1.

    if sinal < 0.:
        x = -1. * x

    # Pega o resto da divisao por 2*PI (1 ciclo)
    x = x - (PI2 * math.trunc(x / PI2))

    ## Se tiver no primeiro quarto do ciclo ja esta ok
    if x < math.pi / 2.:
        return [x, 1. * sinal]
    ## Se tiver no segundo quarto do ciclo devo pegar o complemento para 1*PI
    elif x < math.pi:
        return [math.pi - x, 1. * sinal]
    ## Terceiro quadrante
    elif x < (math.pi * 1.5):
        return [x - math.pi, -1. * sinal]
    ## Quarto e ultimo eh o complemento para 2*PI
    else:
        return [PI2 - x, -1. * sinal]


def calculaFTaylor(x, fator):
    ret = ajusta_x_calculo_seno(x)
    x = ret[0]
    acc = 0.
    for n in range(0, fator + 1):
        n2_1 = (2 * n) + 1
        acc = acc + ((math.pow(-1, n) * math.pow(x, n2_1)) / math.factorial(n2_1))
    return ret[1] * acc


def testes(grau):
    valores = [9. * math.pi / 4., 21 * math.pi / 4., 41 * math.pi / 4.]

    header = r"""
    \begin{table}[h!]
    \centering
    \caption{Testes do Exercicio 3}
    \begin{tabular}{|c|c|c|c|}
    \toprule
    \textbf{$x$} & \textbf{$f(x)$ (com NumPy)} & \textbf{$f(x)$ (com Taylor)} & \textbf{Diferenca} \\
    \midrule   
    """

    tail = r"""
    \bottomrule
    \end{tabular}
    \end{table}    
    """

    # gera tabela com o resultado da comparacao
    with open("../latex/comparacao_exercicio3.tex", "w") as arquivo:
        arquivo.write(header)
        for val in valores:
            val_np = calculaF(val)
            val_taylor = calculaFTaylor(val, grau)
            val_diff = math.fabs(val_np - val_taylor)
            arquivo.write(fr"""{val:.4e} & {val_np:.4e} & {val_taylor:.4e} & {val_diff:.4e} \\
                            """)

        arquivo.write(tail)


def executa_exercicio():
    menor_grau = 0
    for i in range(2, 100):
        r = calcula_residuo1(i)
        print(f"{i};{r[0]};{r[1]};{calcula_residuo2(i)}")
        if r[0]:
            print(f"O menor grau eh {i}")
            menor_grau = i
            break

    testes(menor_grau)

    with open("../dados/exercicio3.csv", "w") as arquivo:
        ## rodar de -PI a PI
        for i in range(0, int(6 * math.pi * 10000)):
            val = float(i / 10000) - (3 * math.pi)

            valFx = calculaF(val)
            valP2 = calculaFTaylor(val, 2)
            valP5 = calculaFTaylor(val, 5)
            valP12 = calculaFTaylor(val, 12)

            str = f"{val};{valFx};{valP2};{valP5};{valP12};{math.fabs(valFx - valP12)}\n"
            arquivo.write(str)


def calcula_residuo1(n):
    C = 7.0 / math.log10(math.pi / 2)
    v = (math.log10(math.factorial(n + 1)) / math.log10(math.pi / 2.)) - (n + 1)
    return [C <= v, v - C]


def calcula_residuo2(n):
    return math.pow(math.pi / 2, n + 1) <= math.factorial(n + 1) * 1E-7


if __name__ == '__main__':
    executa_exercicio()
    print("Fim do processamento.")
