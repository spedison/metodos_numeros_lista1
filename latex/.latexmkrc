$pdf_mode = 1;                # Usa pdflatex
$bibtex_use = 1;              # Usa BibTeX
$interaction = 'nonstopmode';
$synctex = 1;

$out_dir = '.';           # Todos os arquivos compilados vão para ./build
$jobname = 'relatorio';

# Cria o diretório se não existir
# mkdir $out_dir unless -d $out_dir;

# Informa ao latexmk onde procurar os arquivos auxiliares
$aux_dir = $out_dir;