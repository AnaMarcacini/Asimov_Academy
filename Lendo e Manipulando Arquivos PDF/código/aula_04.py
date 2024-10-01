# --- Extrair páginas de um PDF
from pathlib import Path

import pypdf

caminho_pdf = Path('materiais de aula') / 'documentos' / 'vpt_minecraft.pdf'

leitor_pdf = pypdf.PdfReader(caminho_pdf)
pagina = leitor_pdf.pages[4]

escritor_pdf = pypdf.PdfWriter()
escritor_pdf.add_page(pagina)
escritor_pdf.write('vpt_minecraft_p5.pdf')

escritor_pdf = pypdf.PdfWriter()
for pagina in leitor_pdf.pages[:3]:
    escritor_pdf.add_page(pagina)
escritor_pdf.write('vpt_minecraft_intro.pdf')
