from operator import index
import sqlite3
import pandas as pd

conn = sqlite3.connect('web.db')

df_data = pd.read_csv('bd_data.csv', index_col=0)
df_data.index.name = 'index_name'
df_data.to_sql('data', conn, index_label='index_name')#pasar dados do data para sql


c = conn.cursor()
c.execute('CREATE TABLE products (product_id, product_name, price)')
conn.commit()#alguns comandos nescessitam do commit para atualizar o bd nesse caso não é nescessário

c.execute('DROP TABLE products')
c.execute('DROP TABLE data')

c.execute('CREATE TABLE products ([product_id] INTEGER PRIMARY KEY, [product_name] TEXT, [price] INTEGER)')



# INSERT -- inserir itens
c.execute('''INSERT INTO products (product_id, product_name, price)
    VALUES
    (1, 'Computer', 800),
    (2, 'Printer', 200),
    (3, 'Tablet', 300)
''')
conn.commit()#nescessário

df_data2 = df_data.iloc[::-2]#cria uma nova tabela com os ultimos valores sendo os primeiros e pulando de 2 em dois valores
df_data2.to_sql('data', conn, if_exists='append')#caso a tabela exista adiciona no final 

# if_exists : {'fail', 'replace', 'append'}, default 'fail'
#     How to behave if the table already exists.

# fail: Raise a ValueError.
# replace: Drop the table before inserting new values.
# append: Insert new values to the existing table.


# SELECT
c.execute("SELECT * FROM data")
c.fetchone()#mostra o primeiro item da execução
c.fetchall()#mostra tudo apó isso apaga os dados do c
df = pd.DataFrame(c.fetchall())#lê e já salva no pandas


c.execute("SELECT * FROM data WHERE A > 200")
df = pd.DataFrame(c.fetchall())

c.execute("SELECT * FROM data WHERE A > 200 AND B > 100")
df = pd.DataFrame(c.fetchall())


c.execute("SELECT A, B, C FROM data WHERE A > 200 AND B > 100")
df = pd.DataFrame(c.fetchall())


query = "SELECT * FROM data"
df = pd.read_sql(query, con=conn, index_col='index_name')#avisa que a coluna index_name é o indice

df = pd.read_sql("SELECT A, B, C FROM data WHERE A > 200 AND B > 100", con=conn)



# UPDATE e DELETE
c.execute("UPDATE data SET A=218 WHERE index_name='b'")
conn.commit()

c.execute("UPDATE data SET A=220, B=228 WHERE index_name='b'")
conn.commit()

c.execute("DELETE FROM data WHERE index_name=1")  
conn.commit()