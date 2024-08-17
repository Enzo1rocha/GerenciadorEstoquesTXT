from modulos import arquivo
from modulos import produtos
from modulos import estoque

arquivos = ["produtos.txt", "estoque.txt", "logs.txt"]
for i in arquivos:
    arquivo.arqExiste(i)

estoque.adicionar_Produtos_Estoque(arquivos[0], arquivos[1])