def adicionarProdutoNoArquivo(arquivo=".txt", nomedocliente="Desconhecido"):
    try:
        a = open(arquivo, 'r+')
    except:
        print("Ocorreu Algum Erro!!!")
    else:
            lista_Produtos_no_Arquivo = []
            for linha in a:
                clientes = linha.split(';')
                clientes[0].replace("\n","")
                lista_Produtos_no_Arquivo.append(clientes[0])

            if nomedocliente not in lista_Produtos_no_Arquivo:
                a.write(f'{nomedocliente};\n')
                print(f"{nomedocliente} Adicionado Com Sucesso")
    finally:
        a.close()


def adicionar_Manualmente_Produtos_em_Lista(arquivoTXT=".txt"):
        lista = []
        while True:
            nome = str(input("Digite o Nome do Produto: ")).capitalize()
            if nome in lista:
                print("Este Produto ja possui um estoque")
                continue
            else:
                lista.append(nome)
                while True:
                    continuar = str(input("Continuar? [S/N]")).upper()
                    if continuar in ["S","N"]:
                        break
                if continuar == 'S':
                    continue
                else:
                    for i in lista:
                        adicionarProdutoNoArquivo(arquivoTXT, i)
                    break
        