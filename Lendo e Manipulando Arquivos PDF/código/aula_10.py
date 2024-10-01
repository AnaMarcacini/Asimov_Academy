# --- Adicionando senha a um PDF

from pathlib import Path

import pypdf

caminho_pdf = Path('materiais de aula') / 'documentos' / 'dom_casmurro.pdf'
escritor_pdf = pypdf.PdfWriter(clone_from=caminho_pdf)

escritor_pdf.encrypt('senha-secreta')

escritor_pdf.write('dom_casmurro_com_senha.pdf')


# --- Tentando abrir PDF com senha
from pathlib import Path

import pypdf

caminho_pdf = Path('dom_casmurro_com_senha.pdf')
leitor_pdf = pypdf.PdfReader(caminho_pdf)

# A linha abaixo gera erro: FileNotDecryptedError: File has not been decrypted
print(leitor_pdf.pages)


# --- Pegando senha do PDF via input
from pathlib import Path

import pypdf

caminho_pdf = Path('dom_casmurro_com_senha.pdf')
leitor_pdf = pypdf.PdfReader(caminho_pdf)

if leitor_pdf.is_encrypted:
    senha = input('PDF requer senha. Digite a senha do PDF:')
    result = leitor_pdf.decrypt(senha)
    if result == 0:
        print('Senha incorreta')
    else:
        print('Senha correta')
        print(f'O PDF tem {len(leitor_pdf.pages)} páginas.')
else:
    print(f'O PDF tem {len(leitor_pdf.pages)} páginas.')
