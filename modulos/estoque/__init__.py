def adicionar_Cliente_Estoque(arquivoComNomes=".txt", arquivoEndereço='.txt'):
    try:
        a = open(arquivoComNomes, 'rt')
    except:
        print("Erro ao ler o arquivo")
    else:
        for linha in a:
            dado = linha.split(';')
            dado[0] = dado[0].replace('\n', '')
            try:
                arq = open(arquivoEndereço, 'at')
            except:
                print("Ocorreu Algum Erro")
                break
            else:
                try:
                    produto = 'None'
                    quantidade = 0
                    arq.write(f'{dado[0]}:{produto}:{quantidade}\n')
                except:
                    print("Erro na hora de adiconar, produto quantidade e nome")
                else:
                    print(f'Estode de {dado[0]} \nProduto: {produto}\nQuantidade: {quantidade}\nFOI ADICIONADO COM SUCESSO')
            finally:
                arq.close()
    finally:
        a.close()


def alterar_Dados_Cliente(arquivoEstoque='.txt'):
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

