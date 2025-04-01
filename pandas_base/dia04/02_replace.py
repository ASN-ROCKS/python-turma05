# %%

import pandas as pd

df = pd.DataFrame(
    {
        "nome": ["teo", "nah", "ana", "leo", "bia", "teo", "pedro" ],
        "sobrenome": ["calvo", "ataide", "silva", "silva","silva", "calvo", "calvo"],
        "sobrenome_pai": ["balbino", "ataide", "silva", "costa","costa", "calvo", "calvo"],
        "idade": [32, 35, None, 30, None, 32, 32],
        "salario": [3231, 5543, 5332, 6530, 1232, None, None],
    }
)

df = df.replace({
    "sobrenome_pai": {"silva": "costa", "calvo": "balbino"},
    "sobrenome":{"ataide": "gironde"}
})

# %%

df["sobrenome_pai"] = df["sobrenome_pai"].replace({"silva": "costa", "calvo": "balbino"})
df["sobrenome"] = df["sobrenome_pai"].replace({"ataide": "gironde"})
df