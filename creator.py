import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password=""
)

mycursor = mydb.cursor()

#Criar o Database estoque
#mycursor.execute("CREATE DATABASE estoque")


#Selecionar o Database para a criação das tabelas
mycursor.execute("USE estoque")

#Criar as tabelas padrões
#mycursor.execute("CREATE TABLE produtos (id INT AUTO_INCREMENT PRIMARY KEY not null, name VARCHAR(255) not null, sku INT(13) not null, quantidade_atual INT(4) not null, preco_compra DECIMAL(3,2) not null, preco_venda DECIMAL(3,2) not null, estoque_minimo INT(2))")

def ApagarTodasInfoProdutos():

  ApagarTudoProdutos = ("TRUNCATE TABLE produtos")

  mycursor.execute(ApagarTudoProdutos)







nomeColuna1 = "id"
nomeColuna2 = "name"
nomeColuna3 = "sku"
nomeColuna4 = "quantidade_atual"
nomeColuna5 = "preco_compra"
nomeColuna6 = "preco_venda"
nomeColuna7 = "estoque_minimo"














def ProcurarProdutos():
  try:
    query = "SELECT * FROM produtos WHERE sku = %s"
    ProdDesejado = input("Qual o SKU do produto que você deseja procurar? ")
    mycursor.execute(query, ProdDesejado)
    linhas = mycursor.fetchall()
    linhasColuna1 = []
    linhasColuna2 = []
    linhasColuna3 = []
    linhasColuna4 = []
    linhasColuna5 = []
    linhasColuna6 = []
    linhasColuna7 = []
    for i in linhas:
        linhasColuna1.append(i[0]) 
        linhasColuna2.append(i[1])
        linhasColuna3.append(i[2])
        linhasColuna4.append(i[3])
        linhasColuna5.append(i[4])
        linhasColuna6.append(i[3])
        linhasColuna7.append(i[3])
    dataframe = pd.DataFrame()
    dataframe[nomeColuna1] = linhasColuna1
    dataframe[nomeColuna2] = linhasColuna2
    dataframe[nomeColuna3] = linhasColuna3
    dataframe[nomeColuna4] = linhasColuna4
    dataframe[nomeColuna5] = linhasColuna5
    dataframe[nomeColuna6] = linhasColuna6
    dataframe[nomeColuna7] = linhasColuna7
    print(dataframe)
  except:
    print("Produto não encontrado! Voltando para o menu!")

   
def Teste():
  Procurar = ("SELECT * FROM produtos WHERE sku = 1;")
  mycursor.execute(Procurar)
  Resultado = mycursor.fetchall()
  Final = Resultado[0]
  print(f"ID = {Final[0]}")
  print(f"Nome = {Final[1]}")
  print(f"Codigo SKU = {Final[2]}")
  print(f"Quantidade Atual = {Final[3]}")
  print(f"Preço de Compra = R${Final[4]}")
  print(f"Preço de Venda = R${Final[5]}")
  print(f"Estoque mínimo = {Final[6]}")

Teste()
#ProcurarProdutos()