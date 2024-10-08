
from http import client
from json.encoder import INFINITY
import traceback
from uuid import uuid4
from modulos import *
from modulos.entradaDeDados import float_input, int_input
from modulos.logsestoque import AddLog
from modulos.proInterface import limparTerminal
from time import sleep

def avisosEstoque(quantidadeMinimaParaAviso=1000, quantidadeEstoqueCheio=10000, ValorEstoqueAtual=0):
    if ValorEstoqueAtual < quantidadeMinimaParaAviso:
        return "REABASTECER"
    elif ValorEstoqueAtual >= quantidadeEstoqueCheio:
        return "LIMITE DE ESTOQUE"
    else:
        return "NENHUM AVISO"



def adicionar_Produtos_Estoque(arquivoComNomes=".txt", arquivoEndereço='.txt'):
    try:
        a = open(arquivoComNomes, 'rt', encoding="utf-8")
        b = open(arquivoEndereço, 'r+', encoding="utf-8")
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
            arq = open(arquivoEndereço, 'at', encoding="utf-8")
        except:
            print("Ocorreu Algum Erro")
        else:
            try:
                i = 0
                while i < len(lista_produtos):
                    if lista_produtos[i][0] not in lista_Nomes_Estoque:
                        print(f"====== CONFIGURAÇÃO DO ESTOQUE DO PRODUTO {lista_produtos[i][0]} ======")
                        while True:
                            minimo_aviso = int_input("Limite de estoque para aviso para reabastecimento: ")
                            maximo_aviso = int_input("Limite para aviso de estoque cheio")
                            unidade_de_medida = input("Unidade de medida: ")
                            sigla_unidade_medida = input(f"Sigla da unidade de medida {unidade_de_medida}: ")
                            print(f"ESTOQUE TOTAL = {lista_produtos[i][2]}")
                            quantidade_Disponivel = str(int_input(f"Quantidade disponivel do produto {lista_produtos[i][0]}: "))
                            quantidade_Armazenada = str(int_input(f"Quantidade Armazenada do produto {lista_produtos[i][0]}: "))
                            quantidade_Comprometida = str(int_input(f"Quantidade Comprometida do Produto {lista_produtos[i][0]}: "))

                            if int(quantidade_Disponivel) <= int(lista_produtos[i][2]) and int(quantidade_Armazenada) <= int(lista_produtos[i][2]) and int(quantidade_Comprometida) <= int(lista_produtos[i][2]):

                                codigo_produto = str(uuid4())

                                arq.write(f'{codigo_produto}:{lista_produtos[i][0]}:{float(lista_produtos[i][1]):.2f}:{lista_produtos[i][2]}:{int(quantidade_Disponivel)}:{int(quantidade_Armazenada)}:{int(quantidade_Comprometida)}:{unidade_de_medida}:{sigla_unidade_medida}:{avisosEstoque(quantidadeMinimaParaAviso=minimo_aviso, quantidadeEstoqueCheio=maximo_aviso, ValorEstoqueAtual=int(lista_produtos[i][2]))}\n')

                                AddLog(CodigoProduto=codigo_produto, productName=(str(lista_produtos[i][0])), productPreço=float(lista_produtos[i][1]), productEstoqueTotal=int(lista_produtos[i][2]), ProdutoQuantidadeDisponivel=int(quantidade_Disponivel), ProdutoQuantidadeArmazenada=int(quantidade_Armazenada), ProdutoQuantidadeComprometida=int(quantidade_Comprometida), UnidadeDeMedida=str(unidade_de_medida), SiglaUnidadeDeMedida=str(sigla_unidade_medida), AvisoDeEstoqueAtual=avisosEstoque(minimo_aviso, maximo_aviso, int(lista_produtos[i][2])), Motivo="N/A", TipoDeEvento='Adição de Produtos', OqueFoiAlterado='N/A')

                                """AddLog(str(codigo_produto), str(lista_produtos[i][0]), float(lista_produtos[i][1]), int(lista_produtos[i][2]), int(quantidade_Disponivel), int(quantidade_Armazenada), int(quantidade_Comprometida), str(unidade_de_medida), str(sigla_unidade_medida), str(avisosEstoque(minimo_aviso, maximo_aviso, lista_produtos[i][2])))"""

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
        a = open(arquivoEstoque, 'r+', encoding="utf-8")
    except:
        print('Erro na abertura do arquivo')
    else:
        try:
            clientes_E_estoques = []
            if a:
                for linha in a:
                    if ":" in linha:
                        dados = linha.split(":")
                        dados[9] = dados[9].replace('\n','')
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
            

            FoiAlterado = f''

            def alterarNome():
                novoNome = str(input("Novo Nome: ")).capitalize()

                velhoNome = clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração]
                print(f"Velho nome: {velhoNome}")

                alteração = f'Nome: Antigo = {velhoNome}, Novo = {novoNome}'

                FoiAlterado = f'{alteração}'

                clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração] = novoNome

                return FoiAlterado


            def alterarPreco():
                novoPreco = f'{float_input("Novo Preço: R$", True):.2f}'

                velhoPreco = clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração]
                print(f"Velho Preço: {velhoPreco}")

                alteração = f'Preço: Antigo = {velhoPreco}, Novo = {novoPreco}'

                FoiAlterado = f'{alteração}'

                clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração] = novoPreco

                return FoiAlterado

            
            def alterarEstoque():
                novoEstoque = f'{int_input("Novo Estoque: ", True)}'
                velhoEstoque = clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração]
                print(f"Velho Estoque: {velhoEstoque}")

                alteração = f'Estoque Total: Antigo = {velhoEstoque}, Novo = {novoEstoque}'

                FoiAlterado = f'{alteração}'


                clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração] = novoEstoque

                return FoiAlterado


            def alterarEstoqueDisponivel():
                novoEstoqueDisponivel = f'{int_input("Novo Estoque Disponivel: ", True)}'

                velhoEstoque = clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração]
                print(f"Velho Estoque Dispnivel: {velhoEstoque}")


                alteração = f'Estoque Disponivel: Antigo = {velhoEstoque}, Novo = {novoEstoqueDisponivel}'

                FoiAlterado = f'{alteração}'


                clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração] = novoEstoqueDisponivel

                return FoiAlterado


            def alterarEstoqueArmazenada():
                novoEstoqueArmazenado = f'{int_input("Novo Estoque Armazenado: ", True)}'

                velhoEstoque = clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração]
                print(f"Velho Estoque Armazenado: {velhoEstoque}")


                alteração = f'Estoque Armazenado: Antigo = {velhoEstoque}, Novo = {novoEstoqueArmazenado}'

                FoiAlterado = f'{alteração}'


                clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração] = novoEstoqueArmazenado

                return FoiAlterado

            
            def alterarEstoqueComprometido():
                novoEstoqueComprometido = f'{int_input("Novo Estoque Comprometido: ", True)}'

                velhoEstoque = clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração]
                print(f"Velho Estoque Comprometido: {velhoEstoque}")


                alteração = f'Estoque Comprometido: Antigo = {velhoEstoque}, Novo = {novoEstoqueComprometido}'

                FoiAlterado = f'{alteração}'


                clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração] = novoEstoqueComprometido
                
                return FoiAlterado


            def alterarUnidadeDeMedida():
                                    
                velhoUnidadeDeMedida = clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração]
                print(f"Unidade de Medida Atual: {velhoUnidadeDeMedida}")


                novoUnidadeDeMedida = input("Nova Unidade de Medida: ")



                alteração = f'Unidade de Medida: Antiga = {velhoUnidadeDeMedida}, Nova = {novoUnidadeDeMedida}'

                FoiAlterado = f'{alteração}'

                clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração] = novoUnidadeDeMedida

                return FoiAlterado

            
            def alterarSiglaDeMedida():
                                    
                velhoSiglaDeMedida = clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração]
                print(f"Unidade de Medida Atual: {velhoSiglaDeMedida}")

                novoSiglaDeMedida = input("Nova Unidade de Medida: ")

                alteração = f'Sigla de Medida: Antiga = {velhoSiglaDeMedida}, Nova = {novoSiglaDeMedida}'

                FoiAlterado = f'{alteração}'

                clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração] = novoSiglaDeMedida

                return FoiAlterado
            

            try:
                match IndexAlteração:
                    case 1:
                        try:
                            while True:
                                mudarNome = str(input(f"Confirmar Mudança do Nome do Produto {clientes_E_estoques[index_Produto_Que_Sera_Alterado][IndexAlteração]}? [S/N] ")).upper()
                                if mudarNome in ["S","N"]:
                                    break
                            if mudarNome == "S":
                                Motivo_Alteração = input("Motivo da Alteração")
                                FoiAlterado += alterarNome()
                        except Exception as errorNome:
                            print("Erro na alteração nome")
                            print(errorNome.__class__)
                            print(errorNome)

                    case 2:
                        try:
                            while True:
                                mudarPreco = str(input(f"Confirmar Mudança do Preço do Produto {clientes_E_estoques[index_Produto_Que_Sera_Alterado][1]}? [S/N] ")).upper()
                                if mudarPreco in ["S","N"]:
                                    break
                            if mudarPreco == "S":
                                FoiAlterado += alterarPreco()
                        except Exception as errorPreco:
                            print("Erro na alteração do preço")
                            traceback.print_exc()

                    case 3:
                        try:
                            while True:
                                mudarEstoque = str(input(f"Confirmar Mudança do Estoque do Produto {clientes_E_estoques[index_Produto_Que_Sera_Alterado][2]}?  [S/N] ")).upper()
                                if mudarEstoque in ["S","N"]:
                                    break
                            if mudarEstoque == "S":
                                FoiAlterado += alterarEstoque()
                        except Exception as errorEstoque:
                            print("Erro Na Alteração de Estoque")
                            print(errorEstoque.__class__)
                            print(errorEstoque)

                    case 4:
                        try:
                            while True:
                                mudarEstoqueDisponivel = str(input(f"Confirmar Mudança do Estoque Disponivel do Produto {clientes_E_estoques[index_Produto_Que_Sera_Alterado][1]}? [S/N]")).upper()
                                if mudarEstoqueDisponivel in ["S","N"]:
                                    break
                            if mudarEstoqueDisponivel == "S":
                                FoiAlterado += alterarEstoqueDisponivel()
                        except Exception as errorEstoque:
                            print("Erro Na Alteração de Estoque")
                            print(errorEstoque.__class__)
                            print(errorEstoque)

                    case 5:
                        try:
                            while True:
                                mudarEstoqueDisponivel = str(input(f"Confirmar Mudança do Estoque Armazenado do Produto {clientes_E_estoques[index_Produto_Que_Sera_Alterado][1]}? [S/N]")).upper()
                                if mudarEstoqueDisponivel in ["S","N"]:
                                    break
                            if mudarEstoqueDisponivel == "S":
                                FoiAlterado += alterarEstoqueArmazenada()
                        except Exception as errorEstoque:
                            print("Erro Na Alteração de Estoque")
                            print(errorEstoque.__class__)
                            print(errorEstoque)

                    case 6:
                        try:
                            while True:
                                mudarEstoqueDisponivel = str(input(f"Confirmar Mudança do Estoque Armazenado do Produto {clientes_E_estoques[index_Produto_Que_Sera_Alterado][1]}? [S/N]")).upper()
                                if mudarEstoqueDisponivel in ["S","N"]:
                                    break
                            if mudarEstoqueDisponivel == "S":
                                FoiAlterado += alterarEstoqueComprometido()
                        except Exception as errorEstoque:
                            print("Erro Na Alteração de Estoque")
                            print(errorEstoque.__class__)
                            print(errorEstoque)

                    case 7:
                        try:
                            while True:
                                mudarUnidadeDeMedida = str(input(f"Confirmar Mudança da unidade de medida do Produto {clientes_E_estoques[index_Produto_Que_Sera_Alterado][1]}? [S/N]")).upper()
                                if mudarUnidadeDeMedida in ["S","N"]:
                                    break
                            if mudarUnidadeDeMedida == "S":
                                FoiAlterado += alterarUnidadeDeMedida()
                        except Exception as errorUnidadeDeMedida:
                            print("Erro Na Alteração da Unidade de Medida")
                            print(errorUnidadeDeMedida.__class__)
                            print(errorUnidadeDeMedida)

                    case 8:
                        try:
                            while True:
                                mudarSiglaDeMedida = str(input(f"Confirmar Mudança da Sigla de medida do Produto {clientes_E_estoques[index_Produto_Que_Sera_Alterado][1]}? [S/N]")).upper()
                                if mudarSiglaDeMedida in ["S","N"]:
                                    break
                            if mudarSiglaDeMedida == "S":
                                FoiAlterado += alterarSiglaDeMedida()
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
                        arqEstoque = open(arquivoEstoque, 'w', encoding="utf-8")
                    except:
                        print("Impossivel Abrir o arqEstoque")
                    else:
                        count = 0
                        while count < len(clientes_E_estoques):
                            arqEstoque.write(f"{clientes_E_estoques[count][0]}:{clientes_E_estoques[count][1]}:{clientes_E_estoques[count][2]}:{clientes_E_estoques[count][3]}:{clientes_E_estoques[count][4]}:{clientes_E_estoques[count][5]}:{clientes_E_estoques[count][6]}:{clientes_E_estoques[count][7]}:{clientes_E_estoques[count][8]}:{clientes_E_estoques[count][9]}\n")
                            count += 1
                        AddLog(CodigoProduto=str(clientes_E_estoques[index_Produto_Que_Sera_Alterado][0]), productName=str(clientes_E_estoques[index_Produto_Que_Sera_Alterado][1]), productPreço=19.99,productEstoqueTotal=100, ProdutoQuantidadeDisponivel=50, ProdutoQuantidadeArmazenada=30,ProdutoQuantidadeComprometida=20, UnidadeDeMedida='Unidade', SiglaUnidadeDeMedida='UN',AvisoDeEstoqueAtual='Baixo', Motivo=Motivo_Alteração, TipoDeEvento='Alteração de Dados',OqueFoiAlterado=FoiAlterado)

                        

                        """AddLog(CodigoProduto=str(clientes_E_estoques[index_Produto_Que_Sera_Alterado][0]), productName=str(clientes_E_estoques[index_Produto_Que_Sera_Alterado][1]), productEstoqueTotal=int(clientes_E_estoques[index_Produto_Que_Sera_Alterado][2]), ProdutoQuantidadeDisponivel=int(clientes_E_estoques[index_Produto_Que_Sera_Alterado][3]), ProdutoQuantidadeArmazenada=int(clientes_E_estoques[index_Produto_Que_Sera_Alterado][4]), ProdutoQuantidadeComprometida=int(clientes_E_estoques[index_Produto_Que_Sera_Alterado][5]), UnidadeDeMedida=str(clientes_E_estoques[index_Produto_Que_Sera_Alterado][6]), SiglaUnidadeDeMedida=str(clientes_E_estoques[index_Produto_Que_Sera_Alterado][7]), AvisoDeEstoqueAtual=str(clientes_E_estoques[index_Produto_Que_Sera_Alterado][9]), Motivo=str(Motivo_Alteração), TipoDeEvento="Alteração de Dados", OqueFoiAlterado=FoiAlterado)"""
            
                except:
                    print("Erro ao Adicionar os novos dados")
    finally:
        a.close()
        arqEstoque.close()
