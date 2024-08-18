from modulos import entradaDeDados

def adicionarProdutoNoArquivo(arquivo=".txt", nomedoproduto="Desconhecido", precodoproduto=0,quantidadedoproduto=0):
    try:
        a = open(arquivo, 'r+')
    except:
        print("Ocorreu Algum Erro!!!")
    else:
            lista_Produtos_no_Arquivo = []
            for linha in a:
                produtos = linha.split(';')
                produtos[0].replace("\n","")
                lista_Produtos_no_Arquivo.append(produtos[0])

            if nomedoproduto not in lista_Produtos_no_Arquivo:
                a.write(f'{nomedoproduto};{precodoproduto};{quantidadedoproduto}\n')
                print(f"{nomedoproduto} Adicionado Com Sucesso")
    finally:
        a.close()


def adicionar_Manualmente_Produtos_em_Lista(arquivoTXT=".txt"):
        lista_nomes = []
        lista_precos = []
        lista_estoque = []
        while True:
            nome = str(input("Digite o Nome do Produto: ")).capitalize()
            preco = str(entradaDeDados.float_input("Preço do Produto: R$"))
            estoque = str(entradaDeDados.int_input("Quantidade Disponivel: "))
            if nome in lista_nomes:
                print("Este Produto ja possui um estoque")
                continue
            else:
                lista_nomes.append(nome)
                lista_precos.append(preco)
                lista_estoque.append(estoque)
                while True:
                    continuar = str(input("Continuar? [S/N]")).upper()
                    if continuar in ["S","N"]:
                        break
                if continuar == 'S':
                    continue
                else:
                    i = 0
                    while i < len(lista_nomes):
                        adicionarProdutoNoArquivo(arquivoTXT, lista_nomes[i], lista_precos[i], lista_estoque[i])
                        i+=1
                    break
        