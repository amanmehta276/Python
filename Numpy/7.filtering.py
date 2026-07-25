import numpy as np

#Filtering = Chossing ane element

ages=np.array([[21,17,19,20,30,18,65],[39,22,15,99,19,20,21]])

# teen=ages[(ages<18) & (ages>65)]

adults=np.where(ages>=18,ages,0)

print(adults)