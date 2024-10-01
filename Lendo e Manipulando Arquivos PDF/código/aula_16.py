# --- Extraindo tabelas via tabula-py

from pathlib import Path

import tabula

caminho_pdf = Path('materiais de aula') / 'documentos' / 'RI Ambev - 1T23.pdf'
tabelas = tabula.read_pdf(caminho_pdf, pages='all')

print(f'Foram encontradas {len(tabelas)} tabelas no arquivo PDF.')
for i, df in enumerate(tabelas, 1):
    print(f'\n\n---------- Tabela {i} ----------\n')
    print(df)
    df.to_excel(f'Tabela {i}.xlsx')
