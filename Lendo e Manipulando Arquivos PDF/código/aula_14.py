# --- Ver todas as imagens de um PDF
from pathlib import Path

import pypdf

caminho_pdf = Path('materiais de aula') / 'documentos' / 'RI Ambev - 1T23.pdf'
leitor_pdf = pypdf.PdfReader(caminho_pdf)

for page in leitor_pdf.pages:
    for obj_imagem in page.images:
        print(f'{obj_imagem} -> {obj_imagem.name}')


# --- Ver os "dados" de uma imagem (string de bytes!)
from pathlib import Path

import pypdf

caminho_pdf = Path('materiais de aula') / 'documentos' / 'RI Ambev - 1T23.pdf'
leitor_pdf = pypdf.PdfReader(caminho_pdf)

for page in leitor_pdf.pages:
    for obj_imagem in page.images:
        print(f'{obj_imagem}\n{obj_imagem.data}')
        input()


# --- Salvar todas as imagens do PDF em uma pasta específica
from pathlib import Path

import pypdf

caminho_pdf = Path('materiais de aula') / 'documentos' / 'RI Ambev - 1T23.pdf'
leitor_pdf = pypdf.PdfReader(caminho_pdf)

pasta_output = Path('imagens_extraídas')
pasta_output.mkdir(exist_ok=True)

i = 0
for page in leitor_pdf.pages:
    for obj_imagem in page.images:
        extensao = obj_imagem.name.split('.')[-1]
        caminho_output = pasta_output / f'imagem_{i:2d}.{extensao}'
        with open(caminho_output, 'wb') as arquivo_imagem:
            arquivo_imagem.write(obj_imagem.data)
        i += 1
