# --- Salvando uma imagem em um PDF
from pathlib import Path

from PIL import Image

caminho = Path('materiais de aula') / 'assets' / 'cachorro.jpg'
imagem = Image.open(caminho)
imagem.save('cachorro.pdf')


# --- Salvando diversas imagens em um PDF
from pathlib import Path

from PIL import Image

pasta_imagens = Path('materiais de aula') / 'assets'
extensoes = ['.png', '.jpg', '.jpeg']

imagens = []
for caminho in sorted(pasta_imagens.iterdir()):
    if caminho.suffix in extensoes:
        imagem = Image.open(caminho)
        imagens.append(imagem)

primeira_imagem = imagens[0]
demais_imagens = imagens[1:]

primeira_imagem.save('arquivo_saida.pdf', save_all=True, append_images=demais_imagens)


# --- Manipulando PDFs após serem salvos
import pypdf

pdf_imagens = pypdf.PdfReader('arquivo_saida.pdf')
escritor_pdf = pypdf.PdfWriter()

for pagina in pdf_imagens.pages:
    pagina_em_branco = escritor_pdf.add_blank_page(
        width=pypdf.PaperSize.A4.width,
        height=pypdf.PaperSize.A4.height,
    )
    pagina_em_branco.merge_page(pagina, over=True)

escritor_pdf.write('arquivo_saida_A4.pdf')


# --- Dessa forma, as imagens acabaram cortadas. Vamos tentar
# novamente, dessa vez redimensionando as imagens antes
import pypdf

pdf_imagens = pypdf.PdfReader('arquivo_saida.pdf')
escritor_pdf = pypdf.PdfWriter()

for pagina in pdf_imagens.pages:
    pagina_em_branco = escritor_pdf.add_blank_page(
        width=pypdf.PaperSize.A4.width,
        height=pypdf.PaperSize.A4.height,
    )
    if pagina.mediabox.top > pagina.mediabox.right:  # Imagem vertical
        scale = pagina_em_branco.mediabox.top / pagina.mediabox.top * 0.9
    else:  # Imagem horizontal (ou quadrada)
        scale = pagina_em_branco.mediabox.right / pagina.mediabox.right * 0.9
    transformation = pypdf.Transformation().scale(scale)
    pagina_em_branco.merge_transformed_page(pagina, transformation, over=True)

escritor_pdf.write('arquivo_saida_margem.pdf')


# --- Agora falta apenas centralizar a imagem (isto é, fazer uma translação ao final)
import pypdf

pdf_imagens = pypdf.PdfReader('arquivo_saida.pdf')
escritor_pdf = pypdf.PdfWriter()

for pagina in pdf_imagens.pages:
    pagina_em_branco = escritor_pdf.add_blank_page(
        width=pypdf.PaperSize.A4.width,
        height=pypdf.PaperSize.A4.height,
    )
    if pagina.mediabox.top > pagina.mediabox.right:  # Imagem vertical
        scale = pagina_em_branco.mediabox.top / pagina.mediabox.top * 0.9
    else:  # Imagem horizontal (ou quadrada)
        scale = pagina_em_branco.mediabox.right / pagina.mediabox.right * 0.9
    tx = (pagina_em_branco.mediabox.right - pagina.mediabox.right * scale) / 2
    ty = (pagina_em_branco.mediabox.top - pagina.mediabox.top * scale) / 2
    transformation = pypdf.Transformation().scale(scale).translate(tx=tx, ty=ty)
    pagina_em_branco.merge_transformed_page(pagina, transformation, over=True)

escritor_pdf.write('arquivo_saida_centralizado.pdf')
