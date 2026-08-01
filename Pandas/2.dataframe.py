import pandas as pd

# Dataframe =a tabular data structure,row and column

data={"Name":["Bulbasaur","Charmander","Squirtle"],
      "Type":["Grass","Fire","Water"],
      "HP":[45,39,44]}

df=pd.DataFrame(data,index=["Number1","2","3"])

# Add a new column
df["Attack"]=[49,52,48]

# Add a new row=create new dataframe and concate it letter 
new_row=pd.DataFrame([{"Name":"Pikachu","Type":"Electric","HP":35,"Attack":55}],index=["4"])
df=pd.concat([df,new_row])
print(df)