import sqlite3
import pandas as pd

# Extract
# Busca do banco de dados os produtos dos fornecedores relacionados em fornecedores.csv
con = sqlite3.connect('produtos.sqlite3')
cur = con.cursor()

df = pd.read_csv('fornecedores.csv')
fornecedores = tuple(df['id_fornecedor'].tolist())
query = f'SELECT * FROM produtos WHERE fornecedor in {fornecedores}'
res = cur.execute(query)
print(res.fetchall())