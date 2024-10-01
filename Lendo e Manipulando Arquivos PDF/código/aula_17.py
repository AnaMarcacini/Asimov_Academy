# --- Extrair tabelas em um único arquivo Excel

from pathlib import Path

import pandas as pd
import tabula

caminho_pdf = Path('materiais de aula') / 'documentos' / 'RI Ambev - 1T23.pdf'
tabelas = tabula.read_pdf(caminho_pdf, pages='all')

escritor_excel = pd.ExcelWriter('Tabelas Ambev.xlsx')


def ajusta_header(df):
    novo_header = []
    for header_label, first_row_label in zip(df.columns, df.iloc[0]):
        if header_label.startswith('Unnamed'):
            novo_header.append(first_row_label)
        else:
            novo_header.append(f'{header_label} {first_row_label}')
    df.columns = novo_header
    return df.iloc[1:].reset_index(drop=True)


print(f'Foram encontradas {len(tabelas)} tabelas no arquivo PDF.')
for i, df in enumerate(tabelas, 1):
    print(f'\n\n---------- Tabela {i} ----------\n')
    print(df)
    if df.empty or len(df.columns) < 2:
        continue
    for col_name in df:
        if 'Unnamed' in col_name:
            df = ajusta_header(df=df)
            break
    df.to_excel(excel_writer=escritor_excel, sheet_name=f'Tabela {i}')

escritor_excel.close()
