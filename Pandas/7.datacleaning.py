import pandas as pd

df=pd.read_csv(r"c:\Users\Sneha\OneDrive\Documents\AMAN_DEVELOPER\Python.projects\Pandas\Data.csv",index_col="Name")

# df=df.drop(columns=["Legendary"])

print(df)