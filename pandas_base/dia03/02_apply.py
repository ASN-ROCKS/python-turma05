# %%

entrada = input("Entra com alguma coisa aew: ")

def is_venda(produto):
    return produto.lower().startswith("venda de item:")

# is_venda(entrada)

def is_bota(produto:str):
    return produto.lower().count(" bota") > 0

# %%

import pandas as pd

produtos = pd.read_csv("../data/produtos.csv")
produtos

# %%

filtro_venda = []
for i in produtos["descProduto"]:
    filtro_venda.append(is_venda(i))

produtos[filtro_venda]

# %%
produtos["descProduto"].apply(is_venda)

# %%
produtos["descProduto"].apply(lambda x: x.lower().startswith("venda de item:"))

# %%

produtos["descProduto"].str.lower().str.startswith("venda de item:")

# %%

def soma(a, b):
    return a + b

def sub(a,b):
    return a - b

opcao = "soma"

funcoes = {
    "soma": soma,
    "sub": sub,
}

funcoes[opcao](1,1)
