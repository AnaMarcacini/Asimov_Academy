# --- Rotacionando

from pathlib import Path

import pypdf

caminho_pdf = Path('materiais de aula') / 'documentos' / 'vpt_minecraft.pdf'
leitor_pdf = pypdf.PdfReader(caminho_pdf)

escritor_pdf = pypdf.PdfWriter()

for page in leitor_pdf.pages:
    rotated_page = page.rotate(90)
    escritor_pdf.add_page(rotated_page)

escritor_pdf.write('vpt_minecraft_rotacionado_01.pdf')


# --- Agilizando processo: usando argumento clone_from no PdfWriter!

from pathlib import Path

import pypdf

caminho_pdf = Path('materiais de aula') / 'documentos' / 'vpt_minecraft.pdf'
escritor_pdf = pypdf.PdfWriter(clone_from=caminho_pdf)

for page in escritor_pdf.pages:
    page.rotate(-90)

escritor_pdf.write('vpt_minecraft_rotacionado_02.pdf')


# --- Usando um Transformation para rodar conteúdo

from pathlib import Path

import pypdf

caminho_pdf = Path('materiais de aula') / 'documentos' / 'vpt_minecraft.pdf'
escritor_pdf = pypdf.PdfWriter(clone_from=caminho_pdf)

transformation = pypdf.Transformation().rotate(45)

for page in escritor_pdf.pages:
    page.add_transformation(transformation)

escritor_pdf.write('vpt_minecraft_rotacionado_03.pdf')


# --- Adicionando uma translação ao Transformation para tentar centralizar o conteúdo

from pathlib import Path

import pypdf

caminho_pdf = Path('materiais de aula') / 'documentos' / 'vpt_minecraft.pdf'
escritor_pdf = pypdf.PdfWriter(clone_from=caminho_pdf)

transformation = pypdf.Transformation().rotate(30).translate(tx=300)

for page in escritor_pdf.pages:
    page.add_transformation(transformation)

escritor_pdf.write('vpt_minecraft_rotacionado_04.pdf')
