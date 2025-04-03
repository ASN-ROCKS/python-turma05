# %%

import pandas as pd

df_cliente = pd.DataFrame(
    {
        "id": [1, 2, 3, 4, 5, 6, 7 ],
        "nome": ["teo", "nah", "ana", "leo", "bia", "teo", "pedro" ],
        "sobrenome": ["calvo", "ataide", "silva", "silva","silva", "calvo", "calvo"],
        "sobrenome_pai": ["balbino", "ataide", "silva", "costa","costa", "calvo", "calvo"],
        "idade": [32, 35, 32, 30, 30, 32, 32],
        "salario": [3231, 5543, 5332, 6530, 1232, 12345, 23456],
    }
)

df_venda = pd.DataFrame(
    {
        "id": [1,2,3,4,5,6,7,8],
        "idCliente": [1,1,2,2,5,4,3,3],
        "nome": ["A","B","A","C","A","D","A","B"]
    }
)

# select
# from df_cliente as t1
# join df_venda as t2
# on t1.id = t2.idCliente

df_venda.merge(right=df_cliente,
               right_on="id",                
               left_on="idCliente",
               suffixes=["_venda", "_cliente"],
               )