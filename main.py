import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("USE estoque")

nomeColuna1 = "id"
nomeColuna2 = "name"
nomeColuna3 = "sku"
nomeColuna4 = "quantidade_atual"
nomeColuna5 = "preco_compra"
nomeColuna6 = "preco_venda"
nomeColuna7 = "estoque_minimo"

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

def ProcurarProdutos():
  try:
    ParametroLeitura = int(input("Qual parametro você deseja utilizar para a procura?\n1- ID\n2- Codigo SKU\n4- Sair do Programa"))
    if ParametroLeitura == 1:
      Parametro = "id"
    elif ParametroLeitura == 2:
      Parametro = "sku"
    ValorDeProcura = int(input(f"Digite o {Parametro} do produto desejado: "))
    Procurar = (f"SELECT * FROM produtos WHERE {Parametro} = {ValorDeProcura};")
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
  except:
    print("Produto não encontrado! Voltando para o menu!")
    Escolha()


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
        ProcurarProdutos()
      elif Escolha == 3:
        AtualizarInfo()
      elif Escolha == 4:
        DeletarInfo()
      elif Escolha == 5:
        break
    except: 
      print("Digite um dos número válidos!")

Escolha()