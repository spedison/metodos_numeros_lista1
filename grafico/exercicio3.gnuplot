set terminal pngcairo size 1580,1500 enhanced font 'Verdana,13' background rgb "#f5f5f3"
set output "./dados/exercicio3.png"

set datafile separator ";"

set multiplot layout 4,1 title "Comparacao de Aproximacoes - Funcao Seno" font "14"
set xrange [-3*pi:3*pi]
set xtics ( \
    "-3" -3*pi,         "-11/4" -11*pi/4,    "-5/2" -10*pi/4, \
    "-9/4" -9*pi/4,     "-2" -2*pi,          "-7/4" -7*pi/4, \
    "-3/2" -6*pi/4,     "-5/4" -5*pi/4,      "-1" -pi, \
    "-3/4" -3*pi/4,     "-1/2" -pi/2,        "-1/4" -pi/4, \
    "0" 0,              "1/4" pi/4,          "1/2" pi/2, \
    "3/4" 3*pi/4,       "1" pi,              "5/4" 5*pi/4, \
    "3/2" 6*pi/4,       "7/4" 7*pi/4,        "2" 2*pi, \
    "9/4" 9*pi/4,       "5/2" 10*pi/4,       "11/4" 11*pi/4, \
    "3" 3*pi \
)


set key outside

set lmargin 10
set rmargin 10

set title "Funcao Sin(x) para exercicio 3 Com NumPy"
set xlabel "x (multiplos de Pi)"
set ylabel "F(x)"
set yrange [-1.5:1.5]
set style line 1 lt rgb "#000000" lw 1 dt 2
set zeroaxis ls 1
plot \
    "./dados/exercicio3.csv" using 1:2 with lines linewidth 2 linecolor rgb "#1f77b4" notitle

set title "Funcao Sin(x) usando P3(x)"
set xlabel "x (multiplos de Pi)"
set ylabel "P3(x)"
set yrange [-1.5:1.5]
set style line 1 lt rgb "#000000" lw 1 dt 2
set zeroaxis ls 1
plot \
    "./dados/exercicio3.csv" using 1:3 with lines linewidth 2 linecolor rgb "#2faf0e" notitle

set title "Funcao Sin(x) usando P13(x)"
set xlabel "x (multiplos de Pi)"
set ylabel "P13(x)"
set yrange [-1.5:1.5]
set style line 1 lt rgb "#000000" lw 1 dt 2
set zeroaxis ls 1
plot \
    "./dados/exercicio3.csv" using 1:5 with lines linewidth 2 linecolor rgb "#2c002c" notitle


set title "Modulo da Diferenca entre Sin(x) usando numpy e P13(x)"
set xlabel "x (multiplos de Pi)"
set ylabel "Diferenca(x)"
set yrange [0:7e-10]
set style line 1 lt rgb "#000000" lw 1 dt 2
set zeroaxis ls 1
plot \
    "./dados/exercicio3.csv" using 1:6 with lines linewidth 2 linecolor rgb "#2c15FF" notitle

unset multiplot
unset output