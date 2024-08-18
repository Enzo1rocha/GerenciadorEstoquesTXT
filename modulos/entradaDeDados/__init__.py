def int_input(prompt, maiorquezero=False):
    while True:
        try:
            valor = int(input(prompt))
            if maiorquezero:
                if valor >= 0:
                    return valor
                else:
                    print("Valor Inválido ( Valor Negativo )")
            else:
                return valor
        except (ValueError, TypeError):
            print('Valor Inválido ( Não é inteiro )')
        except KeyboardInterrupt:
            print("Nenhuma Entrada Foi Detectada")


def float_input(prompt, maiorquezero=False):
    while True:
        try:
            valor = float(input(prompt))
            if maiorquezero:
                if valor >= 0:
                    return valor
                else:
                    print('Valor Inválido ( Valor Negativo )')
            else:
                return valor
        except (ValueError, TypeError):
            print('Valor Inválido')
        except KeyboardInterrupt:
            print('Nenhuma Entrada Foi Detectada')