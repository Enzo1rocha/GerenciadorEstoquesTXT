def arqExiste(nomedoarquivo=""):
    try:
        a = open(nomedoarquivo, 'rt+')
        a.close()
    except FileNotFoundError:
        try:
            criarArquivo(nomedoarquivo)
        except:
            print("Erro na criação do arquivo")
    else:
        return True
    
def criarArquivo(nomedoarquivo=""):
    try:
        a = open(nomedoarquivo, 'wt+')
        a.close
    except:
        return False
    else:
        return True