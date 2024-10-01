# --- Extrair texto de um PDF nem sempre é infalível!

from pathlib import Path

import pypdf

caminho_pdf = Path('materiais de aula') / 'documentos' / 'dom_casmurro.pdf'
leitor_pdf = pypdf.PdfReader(caminho_pdf)

for i, pagina in enumerate(leitor_pdf.pages, 1):
    print(f' ---------- Página {i:2d}')
    print(pagina.extract_text())
    input()


# --- Dificuldades de ler arquivos com formatação

from pathlib import Path

import pypdf

caminho_pdf = Path('materiais de aula') / 'documentos' / 'RI Ambev - 1T23.pdf'
leitor_pdf = pypdf.PdfReader(caminho_pdf)

for i, pagina in enumerate(leitor_pdf.pages, 1):
    print(f' ---------- Página {i:2d}')
    print(pagina.extract_text())
    input()
