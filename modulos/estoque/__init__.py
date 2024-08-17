def adicionar_Produtos_Estoque(arquivoComNomes=".txt", arquivoEndereço='.txt'):
    try:
        a = open(arquivoComNomes, 'rt')
        b = open(arquivoEndereço, 'r+')
    except:
        print("Erro ao ler o arquivo")
    else:
        lista_Nomes = []
        for linha in a:
            dado = linha.split(';')
            dado[0] = dado[0].replace('\n', '')
            lista_Nomes.append(dado[0])


        lista_Nomes_Estoque = []
        for linhaEstoque in b:
            dadosEstoque = linhaEstoque.split(':')
            lista_Nomes_Estoque.append(dadosEstoque[0])
            
        try:
            arq = open(arquivoEndereço, 'at')
        except:
            print("Ocorreu Algum Erro")
        else:
            try:
                produto = 'None'
                quantidade = 0
                for i in lista_Nomes:
                    if i not in lista_Nomes_Estoque:
                        arq.write(f'{i}:{produto}:{quantidade}\n')
                        print(f'{"="*40}')
                        print(F"Estoque de {i}\nProduto: {produto}\nQuantidade: {quantidade}\nFOI ADICIONADO COM SUCESSO")
            except:
                print("Erro na hora de adiconar, produto quantidade e nome")
            finally:
                arq.close()
    finally:
        a.close()
        b.close()


def alterar_Dados_Produtos(arquivoEstoque='.txt'):
    try:
        a = open(arquivoEstoque, 'rt')
    except:
        print('Erro na abertura do arquivo')
    else:

        try:
            clientes_E_estoques = []

            for linha in a:
                dados = linha.split(':')
                dados[2] = dados[2].replace("\n","")
                clientes_E_estoques.append(dados)

            print(clientes_E_estoques)

        except:
            print("Erro na criação da lista")
    finally:
        a.close()

