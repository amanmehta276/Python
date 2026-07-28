import matplotlib.pyplot as plt
import numpy as np

# print(mpl.__version__)

x=np.array([2023,2024,2025,2026])   #x-axis
y1=np.array([15,25,30,20])   #y-axis
y2=np.array([17,23,38,5])
y3=np.array([13,15,20,5])

line_style=dict(marker=".",markersize=10,markerfacecolor="cyan",markeredgecolor="cyan",
         linestyle="solid",linewidth=1)

plt.plot(x,y1,color="blue",**line_style)  #the plot of graph of x and y

plt.plot(x,y2,color="red",**line_style)  #** unpacks the idictionary

plt.plot(x,y3,color="green",**line_style)
# plt.plot(x,y2)
# plt.plot(y)
# plt.plot(x)
plt.show()  #show the plot graph
# okay this 
a=input()