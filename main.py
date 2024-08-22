from audioop import add
from math import prod
from operator import truediv
from modulos import arquivo
from modulos import produtos
from modulos import estoque
from modulos.logsestoque import addProdutos
from modulos.proInterface import limparTerminal, menuPrincipal

arquivos = ["produtos.txt", "estoque.txt", "logs.txt"]
for i in arquivos:
    arquivo.arqExiste(i)

menu = ["Adicionar Produtos", "Adicionar Produtos No Estoque", "Sair"]


while True:
    limparTerminal()
    opção = menuPrincipal(menu)
    if opção == 1:
        produtos.adicionar_Manualmente_Produtos_em_Lista(arquivos[0])
    elif opção == 2:
        estoque.adicionar_Produtos_Estoque(arquivos[0], arquivos[1])
    elif opção == 3:
        print("Saindo...")
        break