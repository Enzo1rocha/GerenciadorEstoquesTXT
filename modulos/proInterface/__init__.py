from modulos.entradaDeDados import int_input


def limparTerminal():
    import os
    
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def linha(msg='=', tamanho=40):
    print(msg*tamanho)


def cabeçalho(principal, linha='=', tamanho = 40):
    print(linha*tamanho)
    print(principal.center(tamanho))
    print(linha*tamanho)


def menuPrincipal(tituloPrincipal='',lista=[]):
    limparTerminal()
    cabeçalho(tituloPrincipal, '=', 40)
    c = 1
    inicio = c
    for item in lista:
        print(f'{c} - {item}')
        c = c + 1
    fim = c
    linha('=', 40)
    while True:
        try:
            opção = int_input('Opção: ', True)
            if inicio <= opção <= fim:
                return opção
            else:
                print('Escolha Uma Opção Valida')
        except (ValueError, TypeError):
            print('Entrada Invalida')
        except KeyboardInterrupt:
            print('Entrada Inválida')

        
def produtosID():
    try:
        estoqueTXT = open("estoque.txt", 'r')
    except Exception as e:
        print("Erro ao abrir arquivo", e)
    else:
        osIds = []
        Nomes = []
        for linhatxt in estoqueTXT:
            dados = linhatxt.split(':')
            osIds.append(str(dados[0]))
            Nomes.append(str(dados[1]))
        Nomes.append("Voltar")
        opção = menuPrincipal('Produtos', Nomes)
        for i in range(1,len(Nomes)+1):
            if i == opção:
                idDeAlteração = str(osIds[i-1])
        
        return idDeAlteração
    

def opAlteraçãoDados():

    alterações = ["Nome","Preço","Estoque Total", "Estoque Disponivel", "Estoque Armazenado", "Estoque Comprometido", "Unidade de Medida", "Sigla de Medida", "Voltar"]
    opção = menuPrincipal('Opções', alterações)
    c=0
    while c < 8:
        if c == (opção-1):
            retorno = opção
        else:
            retorno = None
        c += 1

    return retorno


            