import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("USE estoque")

def CadastrarProdutos():
    
    try:
      NomeProduto = (input("Digite o nome do produto: "))
      CodigoSKU = int(input("Digite o código SKU do produto: "))
      QuantAtual = int(input("Digite a quantidade atual do produto: "))
      PrecoCompra = float(input("Digite o valor de compra do produto: ")) 
      PrecoVenda = float(input("Digite o valor de venda do produto: "))
      EstoqueMin = int(input("Digite o estoque mínimo do produto: "))

      query = "INSERT INTO produtos (name, sku, quantidade_atual, preco_compra, preco_venda, estoque_minimo) VALUES (%s, %s, %s, %s, %s, %s)"
      values = (NomeProduto, CodigoSKU, QuantAtual, PrecoCompra, PrecoVenda, EstoqueMin)

      mycursor.execute(query, values)
      mydb.commit()


      print("Dados inseridos corretamento")
    except Exception as e:
      print(f"Erro: {e}")


def ApagarTodasInfoProdutos():

  ApagarTudoProdutos = ("TRUNCATE TABLE produtos")

  mycursor.execute(ApagarTudoProdutos)







def MostrarValores():
  mycursor.execute("SELECT * FROM produtos")

  colunas = [i[0] for i in mycursor.description]

  linhas = mycursor.fetchall()

  print(" | ".join(colunas))
  print("-" * 50)
  for linha in linhas:
      print(" | ".join(str(valor) for valor in linha))

CadastrarProdutos()
MostrarValores()


