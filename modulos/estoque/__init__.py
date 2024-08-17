from itertools import count
from os import error
from sys import exception
from uuid import uuid4


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
        for linhaEstoque in b:
            dadosEstoque = linhaEstoque.split(':')
            lista_Nomes_Estoque.append(dadosEstoque[1])
            
        try:
            arq = open(arquivoEndereço, 'at')
        except:
            print("Ocorreu Algum Erro")
        else:
            try:
                i = 0
                while i < len(lista_produtos):
                    if lista_produtos[i][0] not in lista_Nomes_Estoque:
                        arq.write(f'{str(uuid4())}:{lista_produtos[i][0]}:{float(lista_produtos[i][1]):.2f}:{lista_produtos[i][2]}\n')
                        print(f'{"="*40}')
                        print(F"Estoque de {lista_produtos[i][0]}\nPreço unidade: R${float(lista_produtos[i][1]):.2f}\nQuantidade: {lista_produtos[i][2]}\nFOI ADICIONADO COM SUCESSO")
                    i += 1
            finally:
                arq.close()
    finally:
        a.close()
        b.close()


def alterar_Dados_Produtos(arquivoEstoque='.txt', IDproduto="", IndexAlteração=1):
    try:
        a = open(arquivoEstoque, 'r+')
    except:
        print('Erro na abertura do arquivo')
    else:
        try:
            clientes_E_estoques = []
            for linha in a:
                dados = linha.split(':')
                dados[3] = dados[3].replace("\n","")
                clientes_E_estoques.append(dados)
            
            a.close()
        except:
            print("Erro na criação da lista")
        else:
            for produto in clientes_E_estoques:
                if IDproduto in produto:
                    index_Produto_Que_Sera_Alterado = clientes_E_estoques.index(produto)
                    
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
                                mudarNome = str(input(f"Confirmar Mudança do Nome do Produto {clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração]}? ")).upper()
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
                                    novoPreco = str(f"{float(input("Novo Preço: ")):.2f}")

                                    velhoPreco = clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração]
                                    print(f"Velho Preço: {velhoPreco}")

                                    clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração] = novoPreco


                            while True:
                                mudarPreco = str(input(f"Confirmar Mudança do Preço do Produto {clientes_E_estoques[index_Produto_Que_Sera_Alterado][1]}? ")).upper()
                                if mudarPreco in ["S","N"]:
                                    break
                            if mudarPreco == "S":
                                alterarPreco()
                        except Exception as errorPreco:
                            print("Erro na Alteração de Preço")
                            print(errorPreco.__class__)
                            print(errorPreco)

                    case 3:
                        try:
                            def alterarEstoque():
                                    novoEstoque = str(f"{int(input("Nova Quantidade Do Estoque: "))}")

                                    velhoEstoque = clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração]
                                    print(f"Velho Estoque: {velhoEstoque}")


                                    clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração] = novoEstoque


                            while True:
                                mudarEstoque = str(input(f"Confirmar Mudança do Estoque do Produto {clientes_E_estoques[index_Produto_Que_Sera_Alterado][2]}? ")).upper()
                                if mudarEstoque in ["S","N"]:
                                    break
                            if mudarEstoque == "S":
                                alterarEstoque()
                        except Exception as errorEstoque:
                            print("Erro Na Alteração de Estoque")
                            print(errorEstoque.__class__)
                            print(errorEstoque)

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
                        arqEstoque.write(f"{clientes_E_estoques[count][0]}:{clientes_E_estoques[count][1]}:{clientes_E_estoques[count][2]}:{clientes_E_estoques[count][3]}\n")
                        count += 1
                except:
                    print("Erro ao Adicionar os novos dados")
    finally:
        a.close()
