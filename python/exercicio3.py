import math
import numpy as np


def calculaF(x):
    return np.sin(x)


def ajusta_x_calculo_seno(x):
    ## Retorna o intervalo entre 0 PI/2 e o sinal que ele deve ser
    # multiplicado no final. Ex.:[1.45,-1]
    PI2 = math.pi * 2.

    # f(-x) = -f(x)
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


def calculaFTaylor(x, maior_grau):

    # Normaliza a entrada para ficar entre 0 e PI/2
    ret = ajusta_x_calculo_seno(x)
    # Valor "normalizado"
    x = ret[0]
    acc = 0.
    for n in range(0, math.ceil(float(maior_grau) / 2.)):
        n2_1 = (2 * n) + 1
        acc = acc + ((math.pow(-1, n) * math.pow(x, n2_1)) / math.factorial(n2_1))

    # Aplica a simetria da funcao impar (se necessario)
    return ret[1] * acc


def gera_tabela_dos_residuos(grau, erro):
    valores = [n for n in range(3, grau + 2, 2)]

    header = r"""
    \begin{table}[H]
    \centering
    \caption{Testando n com valor do residuo}
    \label{tab:exercicio_3_definir_grau_minimo}
    \begin{tabular}{|c|c|c|}
    \toprule
    \textbf{$n$} & \textbf{Valor do Residuo} & \textbf{Sera usado ?} \\
    \midrule   
    """

    tail = r"""
    \bottomrule
    \end{tabular}
    \end{table}    
    """

    # gera tabela com o resultado da comparacao
    with open("../latex/tabela_residuos_exercicio3.tex", "w") as arquivo:
        arquivo.write(header)
        for n in valores:
            residuo = calcula_residuo(n, erro)
            arquivo.write(fr"""{n} & {residuo[1]:.4e} & {("Sim " if residuo[0] else "Nao")} \\
                            """)
        arquivo.write(tail)


def gera_tabela_comparacao(grau):
    valores = [9. * math.pi / 4., 21 * math.pi / 4., 41 * math.pi / 4.]

    header = r"""
    \begin{table}[h!]
    \centering
    \caption{Testes do Exercicio 3}
    \label{tab:testes_exercicio_3}
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


def calcula_grau_para_erro(erro):
    menor_grau = 0
    for i in range(1, 100, 2):
        r = calcula_residuo(i, erro)
        print(f"N = {i}; Comparacao = {r[0]}; Valor estimado = {r[1]}")
        if r[0]:
            print(f"O menor grau do polinomio eh {i}")
            menor_grau = i
            break
    return menor_grau


def executa_exercicio():
    erro = 0.0000001
    menor_grau = calcula_grau_para_erro(erro)
    gera_tabela_comparacao(menor_grau)
    gera_arquivo_onda_completa(menor_grau)
    gera_tabela_dos_residuos(menor_grau, erro)


def gera_arquivo_onda_completa(menor_grau):
    with open("../dados/exercicio3.csv", "w") as arquivo:
        ## rodar de -PI a PI
        for i in range(0, int(6 * math.pi * 10000)):
            val = float(i / 10000) - (3 * math.pi)

            valFx = calculaF(val)
            valP2 = calculaFTaylor(val, 3)
            valP5 = calculaFTaylor(val, 5)
            val_p_menor_grau = calculaFTaylor(val, menor_grau)

            str = f"{val};{valFx};{valP2};{valP5};{val_p_menor_grau};{math.fabs(valFx - val_p_menor_grau)}\n"
            arquivo.write(str)


def calcula_residuo(n, erro):
    c = math.pow(math.pi / 2., n + 1) / math.factorial(n + 1)
    return [c <= erro, c]


def potencia_loop_teste():
    maior_grau = 13
    for n in range(0, math.ceil(float(maior_grau) / 2.)):
        n2_1 = (2 * n) + 1
        print(f"grau calculado {n2_1} com n = {n}")


if __name__ == '__main__':
    executa_exercicio()
    potencia_loop_teste()
    print("Fim do processamento.")
