# pandas=panel data not 🐼 
# used for machne learning ,data analysis and dta science
# series(1 dimentional) vs dataframe (2 dimentional)

import pandas as pd

# pandas series
# one dimentional array with axis labels
# label data
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64


# data=[1,2,3,4,5]

# # use pd.Series() constructor

# # series=pd.Series(data,index=[1,2,3,4,5])
# series=pd.Series(data,index=["a","b","c","d","e"])
# # series.loc["a"]=6
# # print(series.iloc[1])
# print(series[series>=3])

# calories={"Day 1":1050,"Day 2":2000,"Day 3":2060}
# series=pd.Series(calories)
# print(series.iloc[1])

a=pd.Series(["Bulbasaur","Charmander","Squirtle"],index=[1,2,3])
print(a)