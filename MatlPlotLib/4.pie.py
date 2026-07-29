import matplotlib.pyplot as plt
import numpy as np

categories=["Grains","Fruit","Vegetables","Protein","Dairy","Sweets"]
values=np.array([4,3,2,5,3,1])
colors=["red","blue","yellow","green","orange","purple"]

plt.pie(values,labels=categories,autopct="%1.1f%%",colors=colors,explode=[0,0,0,0,0,0.1],
        shadow=True,startangle=180)

plt.title("Aman Mehta")
plt.show()