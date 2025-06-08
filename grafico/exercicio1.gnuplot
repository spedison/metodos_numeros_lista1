set datafile separator ";"
set key outside
set xlabel "x"
set ylabel "F(x)"
set title "Comparacao de F(x), P1(x), P2(x), P3(x), P4(x)"
set terminal pngcairo size 1280,720 enhanced font 'Verdana,12'
set output "./dados/exercicio1.png"

plot \
    "./dados/exercicio1.csv" using 1:2 with lines linewidth 2 linecolor rgb "#1f77b4" title "F(x)", \
    "./dados/exercicio1.csv" using 1:3 with lines linewidth 2 linecolor rgb "#ff7f0e" title "P1(x)", \
    "./dados/exercicio1.csv" using 1:4 with lines linewidth 2 linecolor rgb "#2ca02c" title "P2(x)", \
    "./dados/exercicio1.csv" using 1:5 with lines linewidth 2 linecolor rgb "#d62728" title "P3(x)", \
    "./dados/exercicio1.csv" using 1:6 with lines linewidth 2 linecolor rgb "#9467bd" title "P4(x)"

unset output