from math import prod
from modulos import arquivo
from modulos import produtos
from modulos import estoque
from modulos.proInterface import limparTerminal

arquivos = ["produtos.txt", "estoque.txt", "logs.txt"]
for i in arquivos:
    arquivo.arqExiste(i)

limparTerminal()
estoque.alterar_Dados_Produtos(arquivos[1], "71f3a87b-7492-4e35-b55f-64b00a8586f5", 7)
estoque.alterar_Dados_Produtos(arquivos[1], "71f3a87b-7492-4e35-b55f-64b00a8586f5", 8)