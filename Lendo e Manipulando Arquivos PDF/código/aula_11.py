# --- Adicionando anotações a um PDF

from pathlib import Path

import pypdf
from pypdf.annotations import FreeText, Text, Rectangle

caminho_pdf = Path('materiais de aula') / 'documentos' / 'dom_casmurro.pdf'
escritor_pdf = pypdf.PdfWriter(clone_from=caminho_pdf)

# Texto livre
texto_livre = FreeText(text="Olá Mundo!\nEsta é uma anotação flutuante!", rect=(400, 550, 550, 600))
escritor_pdf.add_annotation(0, texto_livre)

# Texto em anotação
texto = Text(text="Texto da anotação!", rect=(50, 600, 200, 650))
escritor_pdf.add_annotation(1, texto)

# Linha reta
linha = Rectangle(rect=(50, 550, 200, 650))
escritor_pdf.add_annotation(2, linha)

# Arquivo anexo qualquer (deve ser lido como bytes, modo de leitura "rb")
caminho_imagem = Path('materiais de aula') / 'assets' / 'cachorro.jpg'
with open(caminho_imagem, 'rb') as arquivo:
    dados = arquivo.read()
escritor_pdf.add_attachment('cachorro.jpg', dados)

# Gera PDF com todas as anotações
escritor_pdf.write('dom_casmurro_anotado.pdf')


# --- Lendo anotações de um PDF
leitor_pdf = pypdf.PdfReader("dom_casmurro_anotado.pdf")
for pagina in leitor_pdf.pages:
    if "/Annots" not in pagina:
        continue
    for annot in pagina["/Annots"]:
        print(annot.get_object())


# --- Lendo arquivos em anexo e extraindo seu conteúdo
leitor_pdf = pypdf.PdfReader("dom_casmurro_anotado.pdf")
print(leitor_pdf.attachments)

imagem_bytes = leitor_pdf.attachments['cachorro.jpg'][0]
with open('nova_imagem.jpg', 'wb') as imagem:
    imagem.write(imagem_bytes)
