# --- Redimensionando a página - muda apenas o que é considerado 100%

from pathlib import Path

import pypdf

caminho_pdf = Path('materiais de aula') / 'documentos' / 'vpt_minecraft.pdf'
escritor_pdf = pypdf.PdfWriter(clone_from=caminho_pdf)

for page in escritor_pdf.pages:
    page.scale_by(0.1)

escritor_pdf.write('vpt_minecraft_redimensionado_01.pdf')


# --- Redimensionando a página para um outro tamanho de papel

from pathlib import Path

import pypdf

caminho_pdf = Path('materiais de aula') / 'documentos' / 'vpt_minecraft.pdf'
escritor_pdf = pypdf.PdfWriter(clone_from=caminho_pdf)

for page in escritor_pdf.pages:
    page.scale_to(pypdf.PaperSize.A8.width, pypdf.PaperSize.A8.height)

escritor_pdf.write('vpt_minecraft_redimensionado_02.pdf')


# --- Redimensionando o conteúdo - muda posição do conteúdo na página

from pathlib import Path

import pypdf

caminho_pdf = Path('materiais de aula') / 'documentos' / 'vpt_minecraft.pdf'
escritor_pdf = pypdf.PdfWriter(clone_from=caminho_pdf)

transformation = pypdf.Transformation().scale(sx=1.5, sy=0.5)

for page in escritor_pdf.pages:
    page.add_transformation(transformation)

escritor_pdf.write('vpt_minecraft_redimensionado_03.pdf')


# --- Revertendo processo - conteúdo continua no PDF!

from pathlib import Path

import pypdf

caminho_pdf = Path('vpt_minecraft_redimensionado_03.pdf')
escritor_pdf = pypdf.PdfWriter(clone_from=caminho_pdf)

transformation = pypdf.Transformation().scale(sx=0.666, sy=2)

for page in escritor_pdf.pages:
    page.add_transformation(transformation)

escritor_pdf.write('vpt_minecraft_redimensionado_04.pdf')
