from re import T
import traceback
from uuid import uuid4
from modulos import *
from modulos import proInterface
from modulos.entradaDeDados import float_input, int_input
from modulos.proInterface import limparTerminal
from time import sleep

def adicionar_Produtos_Estoque(arquivoComNomes=".txt", arquivoEndereço='.txt'):
    try:
        a = open(arquivoComNomes, 'rt')
        b = open(arquivoEndereço, 'r+')
    except:
        print("Erro ao ler os arquivos")
    else:
        lista_produtos = []
        for linha in a:
            dado = linha.split(';')
            dado[2] = dado[2].replace('\n', '')
            lista_produtos.append(dado)


        lista_Nomes_Estoque = []
        if b:
            for linhaEstoque in b:
                print(linhaEstoque)
                if ':' in linhaEstoque:
                    dadosEstoque = linhaEstoque.split(':')
                    if len(dadosEstoque) > 1:
                        lista_Nomes_Estoque.append(dadosEstoque[1])
        else:
            print(f"{arquivoEndereço} esta vazio")
        try:
            arq = open(arquivoEndereço, 'at')
        except:
            print("Ocorreu Algum Erro")
        else:
            try:
                i = 0
                while i < len(lista_produtos):
                    if lista_produtos[i][0] not in lista_Nomes_Estoque:
                        print(f"====== CONFIGURAÇÃO DO ESTOQUE DO PRODUTO {lista_produtos[i][0]} ======")
                        while True:
                            unidade_de_medida = input("Unidade de medida: ")
                            sigla_unidade_medida = input(f"Sigla da unidade de medida {unidade_de_medida}: ")
                            quantidade_Disponivel = str(int_input(f"Quantidade disponivel do produto {lista_produtos[i][0]}: "))
                            quantidade_Armazenada = str(int_input(f"Quantidade Armazenada do produto {lista_produtos[i][0]}: "))
                            quantidade_Comprometida = str(int_input(f"Quantidade Comprometida do Produto {lista_produtos[i][0]}: "))

                            if int(quantidade_Disponivel) <= int(lista_produtos[i][2]) and int(quantidade_Armazenada) <= int(lista_produtos[i][2]) and int(quantidade_Comprometida) <= int(lista_produtos[i][2]):

                                arq.write(f'{str(uuid4())}:{lista_produtos[i][0]}:{float(lista_produtos[i][1]):.2f}:{lista_produtos[i][2]}:{int(quantidade_Disponivel)}:{int(quantidade_Armazenada)}:{int(quantidade_Comprometida)}:{unidade_de_medida}:{sigla_unidade_medida}\n')

                                print(F"Estoque de {lista_produtos[i][0]}\nPreço unidade: R${float(lista_produtos[i][1]):.2f}\nQuantidade: {lista_produtos[i][2]}\nFOI ADICIONADO COM SUCESSO")

                                limparTerminal()
                                break
                            else:
                                print(f"Verifique se os dados batem com a quantidade total de estoque do produto {lista_produtos[i][0]} \nQuantidade total de estoque: {lista_produtos[i][2]}")
                                sleep(1)
                                continue
                        
                        #arq.write(f'{str(uuid4())}:{lista_produtos[i][0]}:{float(lista_produtos[i][1]):.2f}:{lista_produtos[i][2]}:{quantidade_Disponivel}:{quantidade_Armazenada}:{quantidade_Comprometida}\n')
                    i += 1
            except Exception as erroNaAdiçãoLista:
                print(erroNaAdiçãoLista)        
            finally:
                a.close()
                b.close()
                arq.close()


def alterar_Dados_Produtos(arquivoEstoque='.txt', IDproduto="", IndexAlteração=1):
    try:
        a = open(arquivoEstoque, 'r+')
    except:
        print('Erro na abertura do arquivo')
    else:
        try:
            clientes_E_estoques = []
            if a:
                for linha in a:
                    if ":" in linha:
                        dados = linha.split(":")
                        dados[8] = dados[8].replace('\n','')
                        clientes_E_estoques.append(dados)
                    else:
                        print("Não Foi Encontrado :")
            else:
                print(f"Arquivo {arquivoEstoque} está vazio")
        except Exception as erroCriaçãoLista:
            print(erroCriaçãoLista)
        else:
            county = 0
            index_Produto_Que_Sera_Alterado = 0
            while county < len(clientes_E_estoques):
                if IDproduto == clientes_E_estoques[county][0]:
                    index_Produto_Que_Sera_Alterado = county
                county += 1
            try:
                match IndexAlteração:
                    case 1:
                        try:
                            def alterarNome():
                                novoNome = str(input("Novo Nome: ")).capitalize()

                                velhoNome = clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração]
                                print(f"Velho nome: {velhoNome}")

                                clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração] = novoNome


                            while True:
                                mudarNome = str(input(f"Confirmar Mudança do Nome do Produto {clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração]}? [S/N] ")).upper()
                                if mudarNome in ["S","N"]:
                                    break
                            if mudarNome == "S":
                                alterarNome()
                        except Exception as errorNome:
                            print("Erro na alteração nome")
                            print(errorNome.__class__)
                            print(errorNome)

                    case 2:
                        try:
                            def alterarPreco():
                                    novoPreco = f'{float_input("Novo Preço: R$", True):.2f}'

                                    velhoPreco = clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração]
                                    print(f"Velho Preço: {velhoPreco}")

                                    clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração] = novoPreco


                            while True:
                                mudarPreco = str(input(f"Confirmar Mudança do Preço do Produto {clientes_E_estoques[index_Produto_Que_Sera_Alterado][1]}? [S/N] ")).upper()
                                if mudarPreco in ["S","N"]:
                                    break


                            if mudarPreco == "S":
                                alterarPreco()
                        except Exception as errorPreco:
                            print("Erro na alteração do preço")
                            traceback.print_exc()

                    case 3:
                        try:
                            def alterarEstoque():
                                    novoEstoque = f'{int_input("Novo Estoque: ", True)}'

                                    velhoEstoque = clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração]
                                    print(f"Velho Estoque: {velhoEstoque}")


                                    clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração] = novoEstoque


                            while True:
                                mudarEstoque = str(input(f"Confirmar Mudança do Estoque do Produto {clientes_E_estoques[index_Produto_Que_Sera_Alterado][2]}?  [S/N] ")).upper()
                                if mudarEstoque in ["S","N"]:
                                    break
                            if mudarEstoque == "S":
                                alterarEstoque()
                        except Exception as errorEstoque:
                            print("Erro Na Alteração de Estoque")
                            print(errorEstoque.__class__)
                            print(errorEstoque)

                    case 4:
                        try:
                            def alterarEstoqueDisponivel():
                                    novoEstoqueDisponivel = f'{int_input("Novo Estoque Disponivel: ", True)}'

                                    velhoEstoque = clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração]
                                    print(f"Velho Estoque Dispnivel: {velhoEstoque}")


                                    clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração] = novoEstoqueDisponivel


                            while True:
                                mudarEstoqueDisponivel = str(input(f"Confirmar Mudança do Estoque Disponivel do Produto {clientes_E_estoques[index_Produto_Que_Sera_Alterado][1]}? [S/N]")).upper()
                                if mudarEstoqueDisponivel in ["S","N"]:
                                    break
                            if mudarEstoqueDisponivel == "S":
                                alterarEstoqueDisponivel()
                        except Exception as errorEstoque:
                            print("Erro Na Alteração de Estoque")
                            print(errorEstoque.__class__)
                            print(errorEstoque)

                    case 5:
                        try:
                            def alterarEstoqueArmazenada():
                                    novoEstoqueArmazenado = f'{int_input("Novo Estoque Armazenado: ", True)}'

                                    velhoEstoque = clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração]
                                    print(f"Velho Estoque Armazenado: {velhoEstoque}")


                                    clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração] = novoEstoqueArmazenado


                            while True:
                                mudarEstoqueDisponivel = str(input(f"Confirmar Mudança do Estoque Armazenado do Produto {clientes_E_estoques[index_Produto_Que_Sera_Alterado][1]}? [S/N]")).upper()
                                if mudarEstoqueDisponivel in ["S","N"]:
                                    break
                            if mudarEstoqueDisponivel == "S":
                                alterarEstoqueArmazenada()
                        except Exception as errorEstoque:
                            print("Erro Na Alteração de Estoque")
                            print(errorEstoque.__class__)
                            print(errorEstoque)

                    case 6:
                        try:
                            def alterarEstoqueComprometido():
                                    novoEstoqueComprometido = f'{int_input("Novo Estoque Comprometido: ", True)}'

                                    velhoEstoque = clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração]
                                    print(f"Velho Estoque Comprometido: {velhoEstoque}")


                                    clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração] = novoEstoqueComprometido


                            while True:
                                mudarEstoqueDisponivel = str(input(f"Confirmar Mudança do Estoque Armazenado do Produto {clientes_E_estoques[index_Produto_Que_Sera_Alterado][1]}? [S/N]")).upper()
                                if mudarEstoqueDisponivel in ["S","N"]:
                                    break
                            if mudarEstoqueDisponivel == "S":
                                alterarEstoqueComprometido()
                        except Exception as errorEstoque:
                            print("Erro Na Alteração de Estoque")
                            print(errorEstoque.__class__)
                            print(errorEstoque)

                    case 7:
                        try:
                            def alterarUnidadeDeMedida():
                                    
                                    velhoUnidadeDeMedida = clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração]
                                    print(f"Unidade de Medida Atual: {velhoUnidadeDeMedida}")


                                    novoUnidadeDeMedida = input("Nova Unidade de Medida: ")

                                    clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração] = novoUnidadeDeMedida


                            while True:
                                mudarUnidadeDeMedida = str(input(f"Confirmar Mudança da unidade de medida do Produto {clientes_E_estoques[index_Produto_Que_Sera_Alterado][1]}? [S/N]")).upper()
                                if mudarUnidadeDeMedida in ["S","N"]:
                                    break
                            if mudarUnidadeDeMedida == "S":
                                alterarUnidadeDeMedida()
                        except Exception as errorUnidadeDeMedida:
                            print("Erro Na Alteração da Unidade de Medida")
                            print(errorUnidadeDeMedida.__class__)
                            print(errorUnidadeDeMedida)

                    case 8:
                        try:
                            def alterarSiglaDeMedida():
                                    
                                    velhoSiglaDeMedida = clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração]
                                    print(f"Unidade de Medida Atual: {velhoSiglaDeMedida}")


                                    novoSiglaDeMedida = input("Nova Unidade de Medida: ")

                                    clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração] = novoSiglaDeMedida


                            while True:
                                mudarSiglaDeMedida = str(input(f"Confirmar Mudança da Sigla de medida do Produto {clientes_E_estoques[index_Produto_Que_Sera_Alterado][1]}? [S/N]")).upper()
                                if mudarSiglaDeMedida in ["S","N"]:
                                    break
                            if mudarSiglaDeMedida == "S":
                                alterarSiglaDeMedida()
                        except Exception as errorSiglaDeMedida:
                            print("Erro Na Alteração da Unidade de Medida")
                            print(errorSiglaDeMedida.__class__)
                            print(errorSiglaDeMedida)

                    case _:
                        print("Erro!!!")
            except Exception as errorAlteração:
                print("Erro na descoberta da alteração")
                print(errorAlteração.__class__)
                print(errorAlteração)
            else:
                try:
                    try:
                        arqEstoque = open(arquivoEstoque, 'w')
                    except:
                        print("Impossivel Abrir o arqEstoque")

                    count = 0
                    while count < len(clientes_E_estoques):
                        arqEstoque.write(f"{clientes_E_estoques[count][0]}:{clientes_E_estoques[count][1]}:{clientes_E_estoques[count][2]}:{clientes_E_estoques[count][3]}:{clientes_E_estoques[count][4]}:{clientes_E_estoques[count][5]}:{clientes_E_estoques[count][6]}:{clientes_E_estoques[count][7]}:{clientes_E_estoques[count][8]}\n")
                        count += 1
                except:
                    print("Erro ao Adicionar os novos dados")
    finally:
        a.close()
        arqEstoque.close()
