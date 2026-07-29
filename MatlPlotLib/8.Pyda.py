import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv(r"c:\Users\Sneha\OneDrive\Documents\AMAN_DEVELOPER\Python.projects\MatlPlotLib\Pokemon.csv")

type_count=df["Type1"].value_counts(ascending=True)
plt.barh(type_count.index,type_count.values,color="#123456",edgecolor="black")
plt.title("# of Pokemons by Primary Type")
plt.xlabel("Count")
plt.ylabel("Type")

plt.tight_layout()
plt.show()