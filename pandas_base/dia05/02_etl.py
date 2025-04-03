# %%

import sqlalchemy
import pandas as pd

engine = sqlalchemy.create_engine("sqlite:///../data/olist.db")

with open("etl.sql") as open_file:
    query = open_file.read()

df = pd.read_sql(query, engine)
df.head()

# %%

from sklearn import cluster

kmeans = cluster.KMeans(n_clusters=5, random_state=42)
kmeans.fit(df[["frequencia", "valor"]])

df["cluster"] =  kmeans.labels_
df

# %%

import matplotlib.pyplot as plt

for i in df["cluster"].unique():
    X = df[df["cluster"]==i]
    plt.scatter(X["frequencia"], X["valor"])

plt.grid(True)

# %%

df.to_sql("seller_cluster", engine, if_exists="replace")