def adicionar_Produtos_Estoque(arquivoComNomes=".txt", arquivoEndereço='.txt'):
    try:
        a = open(arquivoComNomes, 'rt')
        b = open(arquivoEndereço, 'r+')
    except:
        print("Erro ao ler o arquivo")
    else:
        lista_produtos = []
        for linha in a:
            dado = linha.split(';')
            dado[2] = dado[2].replace('\n', '')
            lista_produtos.append(dado)


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
                i = 0
                while i < len(lista_produtos):
                    if lista_produtos[i][0] not in lista_Nomes_Estoque:
                        arq.write(f'{lista_produtos[i][0]}:{float(lista_produtos[i][1]):.2f}:{lista_produtos[i][2]}\n')
                        print(f'{"="*40}')
                        print(F"Estoque de {lista_produtos[i][0]}\nPreço unidade: R${float(lista_produtos[i][1]):.2f}\nQuantidade: {lista_produtos[i][2]}\nFOI ADICIONADO COM SUCESSO")
                    i += 1
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

