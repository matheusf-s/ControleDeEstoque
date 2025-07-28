import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("USE estoque")

def ApagarTodasInfoProdutos():

  ApagarTudoProdutos = ("TRUNCATE TABLE produtos")

  mycursor.execute(ApagarTudoProdutos)


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


      print(f"Novo produto: {NomeProduto}, registrado corretamento")
    except Exception as e:
      print(f"Erro: {e}")

def LerProdutos():
  print("O que você deseja ver?")


def AtualizarInfo():
  print("O que você deseja atualizar?")

def DeletarInfo():
  print("O que você deseja deletar?")

def Escolha():
  while True:
    try:
      Escolha = int(input("Bem-Vindo ao Estoque!!\nO que você deseja realizar?\n1- Cadastrar Novo Produto\n2- Ler Informação\n3- Atualizar Estoque\n4- Deletar Produto!\n5 - Sair do Programa"))
      if Escolha == 1:
        CadastrarProdutos()
      elif Escolha == 2:
        LerProdutos()
      elif Escolha == 3:
        AtualizarInfo()
      elif Escolha == 4:
        DeletarInfo()
      elif Escolha == 5:
        break
    except: 
      print("Digite um dos número válidos!")

Escolha()