# ETL de Pedidos

Aqui você encontrará os detalhes sobre o projeto: como instalar, executar, funcionalidades, recursos e tecnologias utilizadas.

## Introdução

O **ETL de Pedidos** é uma aplicação que recebe um arquivo csv com uma relação de fornecedores e gera pedidos a serem feitos, buscando na tabela de produtos do estoque, quais deles devem ser pedidos. O critério utilizado envolve quantidade em estoque, média mensal de vendas e prazo de entrega. Os pedidos devem ser suficintes para atender a demanda por 3 meses. Produtos cuja quantidade em estoque for maior ou igual à demanda de 3 meses não deve ser pedido.

## Instalação e execução

1. Inicialmente, clone o repositório com o comando `git clone https://github.com/stonefullstm/etl-python`
2. Na raiz do repositório clonado, execute:
 `python -m venv .venv` para criar um ambiente virtual,
 `.venv/Scripts/activate` para ativar o ambiente virtual e 
 `pip install -r requirements.txt` a fim de instalar as dependências
3. Execute `python etl.py` para executar a aplicação

## Tecnologias utilizadas

Linguagem de programação [Pyhton](https://www.python.org/) e o pacote [pandas](https://pandas.pydata.org/).