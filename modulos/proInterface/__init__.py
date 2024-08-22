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


def menuPrincipal(lista):
    cabeçalho('MENU PRINCIPAL', '=', 40)
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