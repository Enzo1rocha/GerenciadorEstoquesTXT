from modulos import arquivo
from modulos import produtos
from modulos import estoque

arquivos = ["produtos.txt", "estoque.txt"]
for i in arquivos:
    arquivo.arqExiste(i)

listacomclientes = []
produtos.adicionar_Manualmente_Produtos_em_Lista(arquivos[0])
estoque.adicionar_Produtos_Estoque(arquivos[0], arquivos[1])