from modulos import arquivo
from modulos import clientes
from modulos import estoque

arquivos = ["clientes.txt", "estoque.txt"]
for i in arquivos:
    arquivo.arqExiste(i)

listacomclientes = []
clientes.adicionar_Manualmente_Clientes_em_Lista(arquivos[0])
estoque.adicionar_Cliente_Estoque(arquivos[0], arquivos[1])