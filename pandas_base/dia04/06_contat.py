# %%

import pandas as pd

df_01 = pd.DataFrame(
    {
        "id": [1, 2, 3, 4, 5, 6, 7 ],
        "nome": ["teo", "nah", "ana", "leo", "bia", "teo", "pedro" ],
        "sobrenome": ["calvo", "ataide", "silva", "silva","silva", "calvo", "calvo"],
        "sobrenome_pai": ["balbino", "ataide", "silva", "costa","costa", "calvo", "calvo"],
        "idade": [32, 35, 32, 30, 30, 32, 32],
        "salario": [3231, 5543, 5332, 6530, 1232, 12345, 23456],
    }
)

df_02 = pd.DataFrame(
    {
        "id": [ 8, 9 ],
        "nome": ["bia", "zé"],
        "sobrenome": ["costa", "barnabé"],
        "idade": [32, 30, ],
        "salario": [ 6530, 1232],
    }
)

# %%

df_01
# %%
df_02

# %%
df_03 = df_01.copy()

# %%

dfs = []
for i in arquivos:
    dfs.append( pd.read_csv(i) )

pd.concat(dfs, ignore_index=True)