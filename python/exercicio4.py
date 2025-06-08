import math
import numpy as np


def criar_termos_polinomio(n):
    return [(-1.) ** i / (2 * i + 1) for i in reversed(range(n))]


def calcular_f_x(x):
    return np.arctan(x)


def calcula_f_x_taylor_com_horner_ajustado(x, n):
    sinal = -1. if x < 0. else 1.
    x = math.fabs(x)

    if x > 1.:
        return (sinal * (math.pi / 2.)) - calcula_f_x_taylor_com_horner(1. / x, n)

    return sinal * calcula_f_x_taylor_com_horner(x, n)


def calcula_f_x_taylor_com_horner(x, n):
    coefs = criar_termos_polinomio(n)
    xp2 = math.pow(x, 2.)
    acc = coefs[0]
    for c in coefs[1:]:
        acc = c + xp2 * acc
    return acc * x


def executar_testes():
    valores_de_testes = [math.pi / 2., math.pi / 3., math.pi / 4.]

    header = r"""
    \begin{table}[h!]
    \centering
    \caption{Testes do Exercicio 4}
    \label{tab:exercicio_4_resultados}
    \begin{tabular}{|c|c|c|c|c|c|}
    \toprule
    \textbf{$x$} & \textbf{$f(x)$ (NP)} & \textbf{$P_{10}(x)$  s/ ajuste} & \textbf{$P_{10}(x)$ c/ ajuste} & \textbf{Dif. sem ajuste} & \textbf{Dif. com ajuste}\\
    \midrule
    
    """

    tail = r"""
    \bottomrule
    \end{tabular}
    \end{table}    
    """

    with open("../latex/comparacao_exercicio4.tex", "w") as arquivo:
        arquivo.write(header)
        for x in valores_de_testes:
            fx = calcular_f_x(x)
            fxta = calcula_f_x_taylor_com_horner_ajustado(x, 10)
            fxt = calcula_f_x_taylor_com_horner(x, 10)
            diff = math.fabs(fx - fxt)
            diffa = math.fabs(fx - fxta)
            arquivo.write(fr"""{x:.4e} & {fx:.4e} & {fxt:.4e} & {fxta:.4e}& {diff:.4e} & {diffa:.4e} \\
                          """)
        arquivo.write(tail)


def executar_exercicio():
    analisa_funcoes_em_range()
    executar_testes()

def analisa_funcoes_em_range():
    #Variaveis para analisar os erros com ajuste
    maior_difereca = 0
    menor_diferenca = math.inf
    x_maior = -1
    x_menor = -1
    contador_erro_menor = 0;
    contador_erro_maior = 0;
    valores_x_com_erros_maiores_que_1pp = []

    # Variaveis para analisar error sem o ajuste
    maior_diferecasa = 0
    menor_diferencasa = math.inf
    x_maiorsa = -1
    x_menorsa = -1
    contador_erro_menorsa = 0;
    contador_erro_maiorsa = 0;
    valores_x_com_erros_maiores_que_1ppsa = []

    ## Para executar a analise entre -300.00 e +300.00
    for x in range(-30000, 30000+1):
        xi = x / 100.

        fx = calcular_f_x(xi)
        fxt = calcula_f_x_taylor_com_horner_ajustado(xi, 10)
        fxtsa = calcula_f_x_taylor_com_horner(xi, 10)
        diff = math.fabs(fx - fxt)
        diffsa = math.fabs(fx - fxtsa)

## Fazendo analise do erro, com os ajustes
        if diff/fx > (1./100.):
            contador_erro_maior += 1
            valores_x_com_erros_maiores_que_1pp.append(xi)
        else:
            contador_erro_menor += 1

        if diff > maior_difereca:
            maior_difereca = diff
            x_maior = xi

        if diff < menor_diferenca:
            menor_diferenca = diff
            x_menor = xi

## Fazendo analise do erro, sem os ajustes
        if diffsa/fx > 0.01:
            contador_erro_maiorsa += 1
            valores_x_com_erros_maiores_que_1ppsa.append(xi)
        else:
            contador_erro_menorsa += 1

        if diffsa > maior_diferecasa:
            maior_diferecasa = diffsa
            x_maiorsa = xi

        if diffsa < menor_diferencasa:
            menor_diferencasa = diff
            x_menorsa = xi


        print(f"{xi}\t{fx}\t{fxt}\t{diff}\n")

    valores_x_com_erros_maiores_que_1pp_abs = [math.fabs(k) for k in valores_x_com_erros_maiores_que_1pp]

    maior_valor_de_erro = max(valores_x_com_erros_maiores_que_1pp_abs)
    menor_valor_de_erro = min(valores_x_com_erros_maiores_que_1pp_abs)

    print(":::::Analise de valores com ajustes:::::")

    print(f"Maior diferenca = {maior_difereca} em {x_maior} com diferenca percentual de {(maior_difereca)/calcular_f_x(x_maior)} ")
    print(f"Menor diferenca = {menor_diferenca} em {x_menor}")

    print(f"Contador de erros maiores que 1% = {contador_erro_maior}")
    print(f"Contador de erros menores que 1% = {contador_erro_menor}")

    print("Caracteristicas do X com erro maior que 1%")
    print("Maior modulo = ", maior_valor_de_erro)
    print("Menor modulo = ", menor_valor_de_erro)

    print(valores_x_com_erros_maiores_que_1pp)

    print(":::::Analise de valores com ajustes:::::")

    valores_x_com_erros_maiores_que_1pp_abssa = [math.fabs(k) for k in valores_x_com_erros_maiores_que_1ppsa]

    maior_valor_de_errosa = max(valores_x_com_erros_maiores_que_1pp_abssa)
    menor_valor_de_errosa = min(valores_x_com_erros_maiores_que_1pp_abssa)

    print(f"Maior diferenca = {maior_diferecasa} em {x_maiorsa} com diferenca percentual de {(maior_difereca)/calcular_f_x(x_maiorsa)} ")
    print(f"Menor diferenca = {menor_diferencasa} em {x_menorsa}")

    print(f"Contador de erros maiores que 1% = {contador_erro_maiorsa}")
    print(f"Contador de erros menores que 1% = {contador_erro_menorsa}")

    print("Caracteristicas do X com erro maior que 1%")
    print("Maior modulo = ", maior_valor_de_errosa)
    print("Menor modulo = ", menor_valor_de_errosa)

    print(valores_x_com_erros_maiores_que_1ppsa)

if __name__ == '__main__':
    executar_exercicio()
    print("Terminado")
