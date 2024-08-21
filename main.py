from math import prod
from modulos import arquivo
from modulos import produtos
from modulos import estoque
from modulos.proInterface import limparTerminal

arquivos = ["produtos.txt", "estoque.txt", "logs.txt"]
for i in arquivos:
    arquivo.arqExiste(i)

limparTerminal()
produtos.adicionar_Manualmente_Produtos_em_Lista(arquivos[0])
estoque.adicionar_Produtos_Estoque(arquivos[0], arquivos[1])