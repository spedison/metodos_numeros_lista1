import math

def calcular_fx(x, n):
    return math.pow(1 + x, n)


def calcular_ftaylor(x, n):
    acc = 0
    for k in range(0, n + 1):
        acc += math.comb(n, k) * math.pow(x, k)

    return acc


def gera_tabela_com_testes(grau):

    header = r"""
    \begin{table}[H]
    \centering
    \caption{Testes do Exercicio 2 com n = 10.}
    \label{tab:exercicio_2_resultados}
    \begin{tabular}{|c|c|c|c|}
    \toprule
    \textbf{$x$} & \textbf{$f(x,10)$} & \textbf{$P_k(x,10)$} & \textbf{Diferenca} \\
    \midrule   
    """

    tail = r"""
    \bottomrule
    \end{tabular}
    \end{table}    
    """

    # gera tabela com o resultado da comparacao
    with open("../latex/comparacao_exercicio2.tex", "w") as arquivo:
        arquivo.write(header)
        for val_x in range(-10, 11):
            val_fx = calcular_fx(val_x, grau)
            val_pkx = calcular_ftaylor(val_x, grau)
            val_diff = math.fabs(val_fx - val_pkx)
            arquivo.write(fr"""{val_x:.4e} & {val_fx:.4e} & {val_pkx:.4e} & {val_diff:.7e} \\
                            """)
        arquivo.write(tail)


def executa_exercicio():
    gera_tabela_com_testes(10)


if __name__ == '__main__':
    executa_exercicio()
    print("Fim do processamento.")
