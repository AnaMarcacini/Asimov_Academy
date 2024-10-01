# --- Combinando dois PDFs diferentes
from pathlib import Path

import pypdf

caminhos = [
    Path('materiais de aula') / 'documentos' / 'dom_casmurro.pdf',
    Path('materiais de aula') / 'documentos' / 'vpt_minecraft.pdf'
]

leitores = [pypdf.PdfReader(caminho) for caminho in caminhos]

indice_pgs = [1, 3, 8]

escritor_pdf = pypdf.PdfWriter()

for indice_pg in indice_pgs:
    for leitor in leitores:
        pagina = leitor.pages[indice_pg]
        escritor_pdf.add_page(pagina)

escritor_pdf.write('documento_intercalado.pdf')
