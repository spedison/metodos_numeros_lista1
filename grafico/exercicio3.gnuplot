set terminal pngcairo size 1580,1200 enhanced font 'Verdana,12'
set output "./dados/exercicio3.png"

set datafile separator ";"
set multiplot layout 4,1 title "Comparacao de Aproximacoes" font ",14"

set key outside

set lmargin 10
set rmargin 10

set title "Funcao Sin(x) para exercicio 3 Com NumPy"
set xlabel "x"
set ylabel "F(x)"
set yrange [-1:1]
plot \
    "./dados/exercicio3.csv" using 1:2 with lines linewidth 2 linecolor rgb "#1f77b4" notitle

set title "Funcao Sin(x) usando P2(x)"
set xlabel "x"
set ylabel "P2(x)"
set yrange [-1:1]
plot \
    "./dados/exercicio3.csv" using 1:3 with lines linewidth 2 linecolor rgb "#2faf0e" notitle

set title "Funcao Sin(x) usando P12(x)"
set xlabel "x"
set ylabel "F(x)"
set yrange [-1:1]
plot \
    "./dados/exercicio3.csv" using 1:5 with lines linewidth 2 linecolor rgb "#2c002c" notitle


set title "Diferenca entre Sin(x) usando numpy e P12"
set xlabel "x"
set ylabel "Diferenca(x)"
set yrange [0:6E-16]
plot \
    "./dados/exercicio3.csv" using 1:6 with lines linewidth 2 linecolor rgb "#2c002c" notitle

unset multiplot
unset output