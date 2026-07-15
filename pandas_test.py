# import pandas as pd
# # df=pd.read_csv("data.csv")

# nums=[1,2,3,4,5]
# df=pd.Series(nums,index=[1,2,3,4,5])
# print(df)

import pandas as pd
import numpy as np
data = [
    {"Name": "Asabeneh", "Country":"Finland","City":"Helsinki"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}]
df = pd.DataFrame(data)
weights=[75,43,54]
df['weight']=weights
df['weight']=df['weight']*1.1
print(df)