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
produtos = res.fetchall()

# Transform
# Gera um pedido para cada fornecedor, suficiente para 3 meses,  baseado no estoque, média de vendas e prazo de entrega de cada produto. Produtos com estoque suficiente para 3 meses não serão pedidos
pedidos = [ (
        produto[7],
        produto[0],
        produto[1],
        produto[5] * 3 - produto[4] + produto[5] * produto[6] // 30
    ) for produto in produtos if produto[4] < produto[5] * 3]

