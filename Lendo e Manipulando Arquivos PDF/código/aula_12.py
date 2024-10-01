# --- Extraindo texto de PDF

from pathlib import Path

import pypdf

caminho_pdf = Path('materiais de aula') / 'documentos' / 'vpt_minecraft.pdf'
leitor_pdf = pypdf.PdfReader(caminho_pdf)

for i, pagina in enumerate(leitor_pdf.pages, 1):
    print(f' ---------- Página {i:2d}')
    print(pagina.extract_text())
    input()


# --- Contando palavras no texto extraído

from collections import Counter
from pathlib import Path

import pypdf

caminho_pdf = Path('materiais de aula') / 'documentos' / 'vpt_minecraft.pdf'
leitor_pdf = pypdf.PdfReader(caminho_pdf)

texto_por_pagina = [pagina.extract_text() for pagina in leitor_pdf.pages]

palavras = []
for texto in texto_por_pagina:
    palavras_pagina = (
        texto
        .lower()
        .replace('\n', ' ')
        .replace(',', ' ')
        .replace('.', ' ')
        .split(' ')
    )
    palavras.extend(palavras_pagina)

contagem = Counter(palavras)
print(contagem)
print(contagem.most_common(20))


# --- Exibe todas as palavras com pelo menos 5 caractere e com 5 ocorrências ou mais
for palavra, cont in sorted(contagem.items(), key=lambda tupla: tupla[1]):
    if len(palavra) >= 5 and cont >= 5:
        print(f'{palavra} -> {cont}')
