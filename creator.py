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