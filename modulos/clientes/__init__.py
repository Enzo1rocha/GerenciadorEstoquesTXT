def adicionarClienteNoArquivo(arquivo="clientes.txt", nomedocliente="Desconhecido"):
    try:
        a = open(arquivo, 'r+')
    except:
        print("Ocorreu Algum Erro!!!")
    else:
            lista_Clientes_no_Arquivo = []
            for linha in a:
                clientes = linha.split(';')
                clientes[0].replace("\n","")
                lista_Clientes_no_Arquivo.append(clientes[0])

            if nomedocliente not in lista_Clientes_no_Arquivo:
                a.write(f'{nomedocliente};\n')
                print(f"{nomedocliente} Adicionado Com Sucesso")
            else:
                print(f"{nomedocliente} Ja Existente")
    finally:
        a.close()


def adicionar_Manualmente_Clientes_em_Lista(arquivoTXT="clientes.txt"):
        lista = []
        while True:
            nome = str(input("Digite o Nome do cliente: ")).capitalize()
            if nome in lista:
                print("Este nome ja é utilizado")
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
                        adicionarClienteNoArquivo(arquivoTXT, i)
                    break
        