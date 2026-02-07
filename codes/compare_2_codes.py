import difflib

# Lendo os arquivos
#with open('codigo1.py', 'r') as f1, open('codigo2.py', 'r') as f2:
with open('mrcm_dd_PASTA_PRINCIPAL.py', 'r') as f1, open('mrcm_dd_PASTA1.py', 'r') as f2:
    texto1 = f1.readlines()
    texto2 = f2.readlines()

# Gerando o relatório HTML
diff = difflib.HtmlDiff().make_file(texto1, texto2, 'Código 1', 'Código 2')

with open('diferencas.html', 'w') as f:
    f.write(diff)

print("Relatório 'diferencas.html' gerado com sucesso.")
