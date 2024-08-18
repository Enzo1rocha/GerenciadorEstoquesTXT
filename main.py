from modulos import arquivo
from modulos import produtos
from modulos import estoque

arquivos = ["produtos.txt", "estoque.txt", "logs.txt"]
for i in arquivos:
    arquivo.arqExiste(i)

estoque.alterar_Dados_Produtos(arquivos[1],"41d93a48-8b4e-4e1c-8d8b-618e147a0e3d", 2)