# --- Explorando o mediabox de um PDF (cortar porções)
from pathlib import Path

import pypdf

caminho_pdf = Path('materiais de aula') / 'documentos' / 'vpt_minecraft.pdf'
leitor_pdf = pypdf.PdfReader(caminho_pdf)

primeira_pagina = leitor_pdf.pages[0]
print('Mediabox original:', primeira_pagina.mediabox)


# Adicionando primeira página no output

escritor_pdf = pypdf.PdfWriter()
escritor_pdf.add_page(primeira_pagina)


# Modificando limites do mediabox diretamente
primeira_pagina.mediabox.left = -200
primeira_pagina.mediabox.right = 800
primeira_pagina.mediabox.top = 792
primeira_pagina.mediabox.bottom = -50
print('Mediabox modificado pelos limites:', primeira_pagina.mediabox)

escritor_pdf.add_page(primeira_pagina)


# Modificando limites do mediabox pelos "cantos"
primeira_pagina.mediabox.lower_left = (100, 220)
primeira_pagina.mediabox.upper_right = (500, 500)
print('Mediabox modificado pelos cantos:', primeira_pagina.mediabox)

escritor_pdf.add_page(primeira_pagina)


escritor_pdf.write('vpt_minecraft_cortado.pdf')
