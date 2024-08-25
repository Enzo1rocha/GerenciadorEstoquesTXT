from audioop import add
from math import prod
from operator import truediv
from time import sleep
from turtle import pensize
from modulos import arquivo
from modulos import produtos
from modulos import estoque
from modulos.logsestoque import AddLog
from modulos.proInterface import limparTerminal, menuPrincipal, opAlteraçãoDados, produtosID

arquivos = ["produtos.txt", "estoque.txt", "logs.txt"]
for i in arquivos:
    arquivo.arqExiste(i)

menu = ["Visualizar Produtos", "Adicionar Produtos", "Visualizar Logs", "Backup", "Sair"]
menu_produtos = ["Adicionar Produtos", "Subir Produtos Para o Estoque", "Alterar Dados no Estoque", "Voltar"]


while True:
    opção = menuPrincipal("MENU PRINCIPAL",menu)
    match opção:
        case 1:
            print("Visualizar Produtos")
        case 2:
            while True:
                opção_produtos = menuPrincipal("PRODUTOS E ESTOQUE", menu_produtos)
                match opção_produtos:
                    case 1:
                        produtos.adicionar_Manualmente_Produtos_em_Lista('produtos.txt')
                    case 2:
                        estoque.adicionar_Produtos_Estoque('produtos.txt', "estoque.txt")
                    case 3:
                        produtoID = produtosID()
                        AlterarOque = opAlteraçãoDados()
                        if AlterarOque == None:
                            break
                        estoque.alterar_Dados_Produtos('estoque.txt',str(produtoID), AlterarOque)
                    case 4:
                        break
        case 3:
            print("Visualizar Logs")
        case 4:
            print("Backup")
        case 5:
            print("Saindo...")
            break