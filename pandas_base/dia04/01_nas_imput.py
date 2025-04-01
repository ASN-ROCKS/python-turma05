# %%

import pandas as pd

df = pd.DataFrame(
    {
        "nome": ["teo", "nah", "ana", "leo", "bia", "teo", "pedro" ],
        "sobrenome": ["calvo", "ataide", "silva", "silva","silva", "calvo", "calvo"],
        "idade": [32, 35, None, 30, None, 32, 32],
        "salario": [3231, 5543, 5332, 6530, 1232, None, None],
    }
)

# %%
media_idade = df["idade"].mean()
media_salario = df["salario"].mean()


# %%
df.fillna({"idade": media_idade , "salario": media_salario})

# %%

medias = df[['idade', 'salario']].mean()
df.fillna(medias)