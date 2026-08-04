import pandas as pd

df=pd.read_csv(r"c:\Users\Sneha\OneDrive\Documents\AMAN_DEVELOPER\Python.projects\Pandas\Data.csv",index_col="Name")

# filtering=keeping the row to match a conditioon

pokemon=df[df["Attack"]>=2]
print(pokemon)