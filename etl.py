import sqlite3

# Extract
con = sqlite3.connect('produtos.sqlite3')
cur = con.cursor()

print('Gerar pedido para um fornecedor')
fornecedor = int(input('Informe o fornecedor: '))
query = f'SELECT * FROM produtos WHERE fornecedor = {fornecedor}'
res = cur.execute(query)
print(res.fetchall())