from math import prod
from modulos import arquivo
from modulos import produtos
from modulos import estoque
from modulos.proInterface import limparTerminal

arquivos = ["produtos.txt", "estoque.txt", "logs.txt"]
for i in arquivos:
    arquivo.arqExiste(i)

limparTerminal()
estoque.alterar_Dados_Produtos('estoque.txt', '4abf34c1-dd65-45c6-af3e-997ca67b6960', 2)