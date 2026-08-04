import pandas as pd

df=pd.read_csv(r"c:\Users\Sneha\OneDrive\Documents\AMAN_DEVELOPER\Python.projects\Pandas\Data.csv",index_col="Name")

# selection by column
# print(df["Name"])

# selection by rows
# print(df.loc[0:2])
# print(df.loc["Pikachu"])

pokemon=input("Enter a Pokemon name : ")
try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found in the dataset")